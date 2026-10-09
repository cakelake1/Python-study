--Задача 1*: Анализ эффективности экспедици
SELECT
    f.expedition_id,
    f.destination,
    f.status,
    (SELECT ROUND(AVG(em.survived) * 100,2)
        FROM expedition_members em
        WHERE em.expedition_id = f.expedition_id)
        AS survival_rate,
    (SELECT SUM(ea.value)
        FROM expedition_artifacts ea
        WHERE ea.expedition_id = f.expedition_id) 
        AS artifacts_value,
    (SELECT COUNT(*)
        FROM expedition_sites es
        WHERE es.expedition_id = f.expedition_id)
        AS discovered_sites,
    (SELECT ROUND(SUM(ec.outcome = 'win')/ COUNT(*) * 100, 2) --тут неизвестно какая строка, возможно succes
        FROM expedition_creatures ec
        WHERE ec.expedition_id = f.expedition_id) 
        AS encounter_success_rate,
    (SELECT SUM(ds.level)
        FROM dwarf_skills ds
        JOIN expedition_members em ON em.dwarf_id = ds.dwarf_id
        WHERE em.expedition_id = f.expedition_id
        AND ds.date BETWEEN f.departure_date AND f.return_date)
        AS skill_improvement,
    DATEDIFF(DAY, f.return_date, f.departure_date) --либо тут простое (f.return_date - f.departure_date)
        AS expedition_duration,
    (SELECT ROUND(AVG(em.survived), 2)
        FROM expedition_members em
        WHERE em.expedition_id = f.expedition_id)
        AS overall_success_score,
    JSON_OBJECT(
        'member_ids',(
            SELECT JSON_ARRAYAGG(em.dwarf_id)
            FROM expedition_members em
            WHERE em.expedition_id = f.expedition_id),
        'artifact_ids', (
            SELECT JSON_ARRAYAGG(ea.artifact_id)
            FROM expedition_artifacts ea
            WHERE ea.expedition_id = f.expedition_id),
        'site_ids', (
            SELECT JSON_ARRAYAGG(es.site_id)
            FROM expedition_sites es
            WHERE es.expedition_id = f.expedition_id) 
        ) AS related_entities
    FROM expeditions f
    WHERE f.status = 'Completed' -- только завершенные задания