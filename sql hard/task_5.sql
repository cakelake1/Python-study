--Задача 2*: Комплексный анализ эффективности производства

WITH workshop_base AS (
    SELECT 
        w.workshop_id,
        w.name AS workshop_name,
        w.type AS workshop_type,
        COUNT(DISTINCT wc.dwarf_id) AS num_craftsdwarves,
        AVG(ds.level) AS average_craftsdwarf_skill,
        COALESCE(SUM(wp.quantity), 0) AS total_quantity_produced,
        COALESCE(SUM(wp.quantity * p.value), 0) AS total_production_value,
        COALESCE(SUM(CASE WHEN wm.is_input = TRUE THEN wm.quantity ELSE 0 END), 0) AS total_material_input,
        MIN(wp.production_date) AS first_date,
        MAX(wp.production_date) AS last_date,
        COUNT(DISTINCT wp.production_date) AS active_days
    FROM workshops w
    LEFT JOIN workshop_craftsdwarves wc ON w.workshop_id = wc.workshop_id
    LEFT JOIN dwarf_skills ds ON wc.dwarf_id = ds.dwarf_id
    LEFT JOIN workshop_products wp ON w.workshop_id = wp.workshop_id
    LEFT JOIN products p ON wp.product_id = p.product_id
    LEFT JOIN workshop_materials wm ON w.workshop_id = wm.workshop_id
    GROUP BY w.workshop_id, w.name, w.type
)
SELECT 
    wb.workshop_id,
    wb.workshop_name,
    wb.workshop_type,
    COALESCE(wb.num_craftsdwarves, 0) AS num_craftsdwarves,
    COALESCE(wb.total_quantity_produced, 0) AS total_quantity_produced,
    COALESCE(wb.total_production_value, 0) AS total_production_value,
    ROUND(COALESCE(wb.total_quantity_produced, 0)::DECIMAL / NULLIF(wb.last_date - wb.first_date + 1, 0), 2) AS daily_production_rate,
    ROUND(COALESCE(wb.total_production_value, 0)::DECIMAL / NULLIF(wb.total_material_input, 0), 2) AS value_per_material_unit,
    ROUND(COALESCE(wb.active_days, 0)::DECIMAL / NULLIF(wb.last_date - wb.first_date + 1, 0) * 100, 2) AS workshop_utilization_percent,
    ROUND(COALESCE(wb.total_quantity_produced, 0)::DECIMAL / NULLIF(wb.total_material_input, 0), 2) AS material_conversion_ratio,
    ROUND(COALESCE(wb.average_craftsdwarf_skill, 0), 2) AS average_craftsdwarf_skill,
    ROUND(COALESCE(wb.average_craftsdwarf_skill * wb.total_production_value / NULLIF(wb.total_quantity_produced, 0), 0), 2) AS skill_quality_correlation,
    JSON_OBJECT(
        'craftsdwarf_ids', (
            SELECT JSON_ARRAYAGG(wc.dwarf_id)
            FROM workshop_craftsdwarves wc
            WHERE wc.workshop_id = wb.workshop_id
        ),
        'product_ids', (
            SELECT JSON_ARRAYAGG(wp.product_id)
            FROM workshop_products wp
            WHERE wp.workshop_id = wb.workshop_id
        ),
        'material_ids', (
            SELECT JSON_ARRAYAGG(wm.material_id)
            FROM workshop_materials wm
            WHERE wm.workshop_id = wb.workshop_id
        ),
        'project_ids', (
            SELECT JSON_ARRAYAGG(p.project_id)
            FROM projects p
            WHERE p.workshop_id = wb.workshop_id
        )
    ) AS related_entities
FROM workshop_base wb
ORDER BY wb.total_production_value DESC;