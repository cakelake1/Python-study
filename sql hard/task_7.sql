    WITH Squad_BASE AS(
        SELECT
            ms.squad_id,
            ms.name,
            ms.formation_type,
            d.name AS leader_name
    FROM military_squads ms
    LEFT JOIN dwarves d ON d.dwarf_id = ms.leader_id
    ),
    Squad_Battles AS(
        SELECT
            squad_id,
            COUNT(sb.report_id) as total_battles,
            SUM(CASE WHEN outcome = 'Victory' THEN 1 ELSE 0 END) AS victories,
            SUM(casualties) AS total_casualties,
            SUM(enemy_casualties) AS total_enemy_casualties,
            ROUND(SUM(COALESCE(enemy_casualties, 0))::DECIMAL
                / NULLIF(SUM(COALESCE(casualties, 0)), 0), 2) AS casualty_exchange_ratio
        FROM squad_battles sb
        GROUP BY squad_id
        ),
    Squad_Members AS(
        SELECT
            squad_id,
            COUNT(sm.dwarf_id) as total_members_ever,
            SUM(CASE WHEN exit_date IS NULL THEN 1 ELSE 0 END) AS current_members
        FROM squad_members sm
        GROUP BY squad_id
    ),
    Squad_Equipment AS(
        SELECT
            sm.squad_id,
            AVG(de.quality::FLOAT) AS avg_equipment_quality
        FROM squad_members as sm
        JOIN dwarf_equipment de ON de.dwarf_id = sm.dwarf_id
        WHERE sm.exit_date IS NULL
        GROUP BY sm.squad_id 
    ),
    Squad_Training AS(
        SELECT
            st.squad_id,
            COUNT(st.schedule_id) AS total_training_sessions,
            AVG(st.effectiveness::FLOAT) AS avg_training_effectiveness
        FROM squad_training st
        GROUP BY squad_id
    ),
    Squad_Skills AS(
        SELECT
            sm.squad_id,
            AVG(ds.level::FLOAT) AS avg_combat_skill_improvement
        FROM squad_members sm
        JOIN dwarf_skills ds ON ds.dwarf_id = sm.dwarf_id
        JOIN skills s ON s.skill_id  = ds.skill_id
        WHERE s.category = 'battle' --предполагаю, что боевая категория навыков
        AND sm.exit_date IS NULL
        GROUP BY sm.squad_id
    )
    SELECT
        sb.squad_id as squad_id,
        sb.name as squad_name,
        sb.formation_type,
        sb.leader_name, 
        COALESCE(bt.total_battles, 0) AS total_battles,
        COALESCE(bt.victories, 0) AS victories,
        ROUND(COALESCE(bt.victories, 0)::DECIMAL
        / NULLIF(bt.total_battles, 0) * 100, 2) AS victory_percentage,
        ROUND(COALESCE(bt.total_casualties, 0)::DECIMAL
        / NULLIF(mm.current_members, 0) * 100, 2) AS casualty_rate
        ROUND(COALESCE(bt.total_enemy_casualties, 0)::DECIMAL
        / NULLIF(bt.total_casualties, 0), 2) AS casualty_exchange_ratio,
        COALESCE(mm.current_members, 0) as current_members,
        COALESCE(mm.total_members_ever, 0) AS total_members_ever,
        ROUND(COALESCE(mm.current_members, 0)::DECIMAL
        / NULLIF(mm.total_members_ever, 0) * 100, 2) AS retention_rate,
        ROUND(COALESCE(se.avg_equipment_quality, 0), 2) AS avg_equipment_quality,
        COALESCE(st.total_training_sessions, 0) AS total_training_sessions,
        ROUND(COALESCE(st.avg_training_effectiveness, 0), 2) AS avg_training_effectiveness,
        ROUND(COALESCE(sk.avg_combat_skill_improvement, 0), 2) AS avg_combat_skill_improvement,
        CORR(st.avg_training_effectiveness, sk.avg_combat_skill_improvement) AS trainig_battle_correlation,
        -- тут должна быть формула для overall effectiveness_score, пока не понимаю как ее рассчитать
        JSON_OBJECT(
        'member_ids', (
            SELECT JSON_ARRAYAGG(sm2.dwarf_id)
            FROM squad_members sm2
            WHERE sm2.squad_id = sb.squad_id
              AND sm2.exit_date IS NULL
        ),
        'equipment_ids', (
            SELECT JSON_ARRAYAGG(de2.equipment_id)
            FROM squad_members sm3
            JOIN dwarf_equipment de2 ON de2.dwarf_id = sm3.dwarf_id
            WHERE sm3.squad_id = sb.squad_id
              AND sm3.exit_date IS NULL
        ),
        'battle_report_ids', (
            SELECT JSON_ARRAYAGG(b2.report_id)
            FROM squad_battles b2
            WHERE b2.squad_id = sb.squad_id
        ),
        'training_ids', (
            SELECT JSON_ARRAYAGG(t2.schedule_id)
            FROM squad_training t2
            WHERE t2.squad_id = sb.squad_id
        )
    ) AS related_entities
FROM Squad_BASE sb
LEFT JOIN Squad_Battles bt ON bt.squad_id = sb.squad_id
LEFT JOIN Squad_Members mm ON mm.squad_id = sb.squad_id
LEFT JOIN Squad_Equipment se ON se.squad_id = sb.squad_id
LEFT JOIN Squad_Training st ON st.squad_id = sb.squad_id
LEFT JOIN Squad_Skills sk ON sk.squad_id = sb.squad_id
ORDER BY sb.squad_id;