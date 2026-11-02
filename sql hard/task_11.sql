-- Задача 5*: Многофакторный анализ угроз и безопасности крепости
Разработайте запрос, который комплексно анализирует безопасность крепости, учитывая:
- Историю всех атак существ и их исходов
- Эффективность защитных сооружений
- Соотношение между типами существ и результативностью обороны
- Оценку уязвимых зон на основе архитектуры крепости
- Корреляцию между сезонными факторами и частотой нападений
- Готовность военных отрядов и их расположение
- Эволюцию защитных способностей крепости со временем

WITH attack_base AS(
    SELECT
        ca.attack_id,
        ca.creature_id,
        ca.date,
        ca.casualties,
        ca.enemy_casualties,
        ca.location_id AS zone_id,
        ca.outcome,
        ca.defense_structures_used,
        ca.military_response_time_minutes,
        c.type AS creature_type,
        c.threat_level,
        c.estimated_population,
        l.name AS zone_name,
        l.fortification_level,
        l.wall_integrity
    FROM creature_attacks ca
    JOIN creatures c ON c.creature_id = ca.creature_id
    LEFT JOIN locations l ON l.location_id = ca.location_id
),
active_threats AS(
    SELECT
        c.type AS creature_type,
        MAX(c.threat_level) AS threat_level,
        MAX(cs.date) AS last_sighting_date,
        MIN(ct.distance_to_fortress) AS territory_proximity,
        SUM(c.estimated_population) AS estimated_numbers,
        JSON_ARRAYAGG(c.creature_id ORDER BY c.creature_id) AS creature_ids
    FROM creatures c
    LEFT JOIN creature_sightings cs ON cs.creature_id = c.creature_id
    LEFT JOIN creature_territories ct ON ct.creature_id = c.creature_id
    WHERE c.active = 1
    GROUP BY c.type
),
vulnerability AS (
    SELECT
        l.location_id as zone_id,
        l.name AS zone_name,
        l.fortification_level,
        COUNT(CASE WHEN ab.outcome = 'Breached' THEN ab.attack_id END) AS historical_breaches,
        ROUND(AVG(ab.military_response_time_minutes),0) AS military_response_time,
        (SELECT JSON_ARRAYAGG(ds.structure_id ORDER BY ds.structure_id)
        FROM defense_structures ds
        WHERE ds.location_id = l.location_id) AS structure_ids,
        (SELECT JSON_ARRAYAGG(ms.squad_id ORDER BY ms.squad_id)
        FROM military_stations ms
        WHERE ms.location_id = l.location_id) AS squad_ids
    FROM locations l
    LEFT JOIN attack_base ab ON ab.zone_id = l.location_id
    GROUP BY l.location_id, l.name, l.fortification_level

),
defense_eff AS(
    SELECT
        ab.defense_structures_used AS defense_type,
        ROUND(SUM(CASE WHEN ab.outcome = 'Repelled' THEN 1 ELSE 0 END)::DECIMAL / NULLIF(COUNT(ab.attack_id), 0) * 100, 2) AS effectiveness_rate,
        ROUND(AVG(ab.enemy_casualties), 1) AS avg_enemy_casualties,
        (SELECT JSON_ARRAYAGG(ds.structure_id ORDER BY ds.structure_id)
        FROM defense_structures ds
        WHERE ds.defense_type = ab.defense_structures_used) AS structure_ids
    FROM attack_base ab
    WHERE ab.defense_structures_used IS NOT NULL
    GROUP BY ab.defense_structures_used
),
squad_readiness AS(
    SELECT
        ms.squad_id,
        ms.name AS squad_name,
        (SELECT COUNT(DISTINCT sm.dwarf_id)
        FROM squad_members sm
        WHERE sm.squad_id = ms.squad_id AND sm.exit_date IS NULL) AS active_members,
        (SELECT ROUND(AVG(ds.level::FLOAT), 1)
         FROM squad_members sm
         JOIN dwarf_skills ds ON ds.dwarf_id = sm.dwarf_id
         JOIN skills s ON s.skill_id  = ds.skill_id AND s.category IN ('Combat', 'Military')
         WHERE sm.squad_id = ms.squad_id AND sm.exit_date IS NULL) AS avg_combat_skill,
        (SELECT COUNT(sb.report_id)
         FROM squad_battles sb
         WHERE sb.squad_id = ms.squad_id) AS total_battles,
        (SELECT SUM(CASE WHEN sb.outcome = 'Victory' THEN 1 ELSE 0 END)
         FROM squad_battles sb
         WHERE sb.squad_id = ms.squad_id) AS victories
    FROM military_squads ms
),
squad_zone_response AS (
    SELECT
        mcz.squad_id,
        mcz.zone_id,
        mcz.response_time
    FROM military_coverage_zones mcz
),
security_evo AS (
    SELECT
        EXTRACT(YEAR FROM ab.date) AS year,
        COUNT(ab.attack_id) AS total_attacks,
        SUM(ab.casualties)AS casualties,
        ROUND(SUM(CASE WHEN ab.outcome = 'Repelled' THEN 1 ELSE 0 END)::DECIMAL/NULLIF(COUNT(ab.attack_id), 0) * 100, 2) AS defense_success_rate
    FROM attack_base ab
    WHERE ab.date IS NOT NULL
    GROUP BY EXTRACT(YEAR FROM ab.date)
)
SELECT JSON_OBJECT(
    'total_recorded_attacks', (
        SELECT COUNT(attack_id)
        FROM attack_base
        ),
    'unique_attackers', (
        SELECT COUNT(DISTINCT creature_id)
        FROM attack_base
        ),
    'overall_defense_success_rate', (
        SELECT ROUND(SUM(CASE WHEN outcome = 'Repelled' THEN 1 ELSE 0 END)::DECIMAL/NULLIF(COUNT(attack_id), 0) * 100, 2) 
        FROM attack_base
        ),
    'current_threat_level', NULL, -- не нашел информации, нужно проверить в эталонном решении
    'active_threats', (
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
                'creature_type', at.creature_type,
                'threat_level', at.threat_level,
                'last_sighting_date', at.last_sighting_date,
                'territory_proximity', at.territory_proximity,
                'estimated_numbers', at.estimated_numbers,
                'creature_ids', at.creature_ids
            )
            ORDER BY at.threat_level DESC, at.creature_type
        )
        FROM active_threats at    
        ),
    'vulnerability_analysis', (
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
                'zone_id', v.zone_id,
                'zone_name', v.zone_name,
                'vulnerability_score', NULL, --тут должна быть формула из эталона
                'historical_breaches', v.historical_breaches,
                'fortification_level', v.fortification_level,
                'military_response_time', v.military_response_time,
                'defense_coverage', JSON_OBJECT(
                    'structure_ids', COALESCE(v.structure_ids, JSON_ARRAY()),
                    'squad_ids', COALESCE(v.squad_ids, JSON_ARRAY())
                )
            )
            ORDER BY v.zone_id
            )
        FROM vulnerability v
    ),
    'defense_effectiveness', (
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
                'defense_type', de.defense_type,
                'effectiveness_rate', de.effectiveness_rate,
                'avg_enemy_casualties', de.avg_enemy_casualties,
                'structure_ids', COALESCE(de.structure_ids, JSON_ARRAY())
            )
            ORDER BY de.effectiveness_rate DESC
        )
        FROM defense_eff de
    ),
    'military_readiness_assessment', (
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
                'squad_id', sr.squad_id,
                'squad_name', sr.squad_name,
                'readiness_score', NULL, -- тут тоже эталонная формула должна быть
                'active_members', sr.active_members,
                'avg_combat_skill', sr.avg_combat_skill,
                'combat_effectiveness', ROUND(COALESCE(sr.victories::DECIMAL/NULLIF(sr.total_battles,0),0),2),
                'response_coverage', (
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'zone_id', szr.zone_id,
                            'response_time', szr.response_time
                        )
                        ORDER BY szr.zone_id
                    )
                    FROM squad_zone_response szr
                    WHERE szr.squad_id = sr.squad_id
                )
            )
            ORDER BY sr.squad_id
        )
        FROM squad_readiness sr
    ),
    'security_evolution', (
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT(
                'year', se.year,
                'defense_success_rate', se.defense_success_rate,
                'total_attacks', se.total_attacks,
                'casualties', se.casualties,
                'year_over_year_improvement', NULL -- посмотреть в эталоне
            )
            ORDER BY se.year
        )
        FROM security_evo se
    )
) AS result
FROM (SELECT 1) AS dummy;