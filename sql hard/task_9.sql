-- Задача: Комплексный анализ торговых отношений и их влияния на крепость
WITH Fortress_Trade AS(
    SELECT
        COUNT(DISTINCT c.civilization_type) AS total_trading_partners,
        SUM(tt.value) AS all_time_trade_value,
        SUM(CASE WHEN tt.balance_direction = 'export' THEN tt.value
        WHEN tt.balance_direction = 'import' THEN -tt.value ELSE 0 END) as all_time_trade_balance
    FROM trade_transactions tt
    JOIN caravans c ON c.caravan_id = tt.caravan_id
),
Civilization_Trade AS(
    SELECT
        c.civilization_type,
        COUNT(DISTINCT c.caravan_id) AS total_caravans,
        SUM(tt.value) AS total_trade_value,
        SUM(CASE WHEN tt.balance_direction = 'export' THEN tt.value
        WHEN tt.balance_direction = 'import' THEN -tt.value ELSE 0 END) as trade_balance
    FROM caravans c
    LEFT JOIN trade_transactions tt ON tt.caravan_id = c.caravan_id
    GROUP BY c.civilization_type
),
Civilization_Caravans AS(
    SELECT
        civilization_type,
        JSON_ARRAYAGG(caravan_id) AS caravan_ids
        FROM caravans
        GROUP BY civilization_type
),
Diplamatic_Trade AS(
    SELECT
        c.civilization_type,
        tt.transaction_id,
        tt.value AS trade_value,
            (SELECT de.relationship_change
            FROM diplomatic_events de
            WHERE de.civilization_type = c.civilization_type
            AND de.date > tt.date) AS relationship_change
    FROM trade_transactions tt
    JOIN caravans c ON c.caravan_id = tt.caravan_id
),
Diplomatic_Corr AS(
    SELECT 
        civilization_type,
        CORR(trade_value, relationship_change) AS diplomatic_correlation
    FROM Diplamatic_Trade
    GROUP BY civilization_type    
),
Import_Trade AS (
    SELECT
        cg.material_type,
        SUM(cg.quantity * cg.value * COALESCE(cg.price_fluaction, 1))::DECIMAL AS dependency_score,
        SUM(cg.quantity) AS total_imported,
        COUNT(DISTINCT cg.original_product_id) AS import_diversity
        FROM caravan_goods cg
        WHERE cg.type = 'import'
        GROUP by cg.material_type
),
Import_dep AS (
    SELECT
    it.material_type,
    it.dependency_score,
    it.total_imported,
    it.import_diversity,
    (
        SELECT JSON_ARRAYAGG(DISTINCT r.resource_id)
        FROM resources r
        WHERE r.type = it.material_type
    ) AS resource_ids
    FROM Import_Trade it
    ORDER BY it.dependency_score DESC
),
Produced_by_Workshop AS(
    SELECT
        w.workshop_id,
        w.type AS workshop_type,
        p.type AS product_type,
        SUM(wp.quantity) AS total_produced
    FROM workshops w
    JOIN workshop_products wp ON wp.workshop_id = w.workshop_id
    JOIN products p ON p.product_id = wp.product_id
    GROUP BY w.workshop_id,w.type,p.type
),
Exported_by_Workshop AS(
    SELECT
        p.workshop_id,
        p.type AS product_type,
        SUM(cg.quantity) AS total_exported,
        AVG(cg.value::DECIMAL / NULLIF(p.value,0)) AS avg_markup
    FROM caravan_goods cg
    JOIN caravans c ON c.caravan_id = cg.caravan_id
    JOIN products p ON p.product_id = cg.original_product_id
    WHERE cg.type = 'export'
    GROUP BY p.workshop_id, p.type
),
Export_Effectiveness AS(
    SELECT
        pr.workshop_type,
        pr.product_type,
        ROUND(COALESCE(ex.total_exported, 0 )::DECIMAL / NULLIF(pr.total_produced, 0 ) * 100,2) AS export_ratio,
        ROUND(COALESCE(ex.avg_markup, 0), 2) AS avg_markup,
        JSON_ARRAYAGG(pr.workshop_id) AS workshop_ids
    FROM Produced_by_Workshop pr
    LEFT JOIN Exported_by_Workshop ex ON ex.workshop_id = pr.workshop_id AND ex.product_type = pr.product_type
    GROUP BY pr.workshop_type, pr.product_type, pr.total_produced, ex.total_exported, ex.avg_markup
),
Timeline_Trade AS(
    SELECT
        EXTRACT(YEAR FROM tt.date) AS year,
        EXTRACT(QUARTER FROM tt.date) AS quarter,
        SUM(tt.value) AS quarterly_value,
        SUM(CASE WHEN tt.balance_direction = 'export' THEN tt.value
        WHEN tt.balance_direction = 'import' THEN -tt.value ELSE 0 END) as quarterly_balance,
        COUNT(DISTINCT c.civilization_type) AS trade_diversity
    FROM trade_transactions tt
    JOIN caravans c on c.caravan_id = tt.caravan_id
    GROUP BY EXTRACT(YEAR FROM tt.date), EXTRACT(QUARTER FROM tt.date)

)
SELECT JSON_OBJECT(
    'total_trading_partners', (SELECT total_trading_partners FROM Fortress_Trade),
    'all_time_trade_value', (SELECT all_time_trade_value FROM Fortress_Trade),
    'all_time_trade_balance', (SELECT all_time_trade_balance FROM Fortress_Trade),
    'civilization_data', JSON_OBJECT('civilisation_trade_data', (
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
                'civilization_type', ct.civilization_type,
                'total_caravans', ct.total_caravans,
                'total_trade_value', ct.total_trade_value,
                'trade_balance', ct.trade_balance,
                'trade_relationship', CASE WHEN ct.trade_balance > 0 THEN 'Favorable'
                WHEN ct.trade_balance < 0 THEN 'Unfavorable' ELSE 'Neutral'END,
                'diplomatic_correlation', ROUND(COALESCE(dc.diplomatic_correlation, 0), 2),
                'caravan_ids', COALESCE(cv.caravan_ids, JSON_ARRAY())
            )
            ORDER BY ct.civilization_type
        )
        FROM Civilization_Trade ct
        LEFT JOIN Diplomatic_Corr dc ON dc.civilization_type = ct.civilisation_type
        LEFT JOIN Civilization_Caravans cv ON cv.civilisation_type = ct.civilisation_type
    )
    ),
    'critical_import_dependencies', JSON_OBJECT(
        'resource_dependency', (
            SELECT JSON_ARRAYAGG(
                JSON_OBJECT(
                    'material_type', d.material_type,
                    'dependency_score', d.dependency_score,
                    'total_imported', d.total_imported,
                    'import_diversity', d.import_diversity,
                    'resource_ids', COALESCE(d.resource_ids, JSON_ARRAY())
                )
                ORDER BY d.dependency_score DESC
            )
            FROM Import_dep d
        )
    ),
    'export_effectiveness', JSON_OBJECT(
        'export_effectiveness', (
            SELECT JSON_ARRAYAGG(
                JSON_OBJECT(
                    'workshop_type', ee.workshop_type,
                    'product_type', ee.product_type,
                    'export_ratio', ee.export_ratio,
                    'avg_markup', ee.avg_markup,
                    'workshop_ids', ee.workshop_ids
                )
                ORDER BY ee.export_ratio DESC
            )
            FROM export_effectiveness ee
        )
    ),
    'trade_timeline', JSON_OBJECT(
        'trade_growth', (
            SELECT JSON_ARRAYAGG(
                JSON_OBJECT(
                    'year', tl.year,
                    'quarter', tl.quarter,
                    'quarterly_value', tl.quarterly_value,
                    'quarterly_balance', tl.quarterly_balance,
                    'trade_diversity', tl.trade_diversity
                )
                ORDER BY tl.year, tl.quarter
            )
            FROM Timeline_Trade tl
        )
    )
) AS result
