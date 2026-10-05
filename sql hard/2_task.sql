--Задача 2: Получение данных о гноме с навыками и назначениями
SELECT 
    f.dwarf_id,
    f.name,
    f.age,
    f.profession,
    JSON_OBJECT(
        'skill_ids', (
            SELECT JSON_ARRAYAGG(d.skill_id)
            FROM dwarf_skills d
            WHERE d.dwarf_id = f.dwarf_id
        ),
        'assignment_ids',(
            SELECT JSON_ARRAYAGG(da.assignment_id)
            FROM dwarf_assignments da
            WHERE da.dwarf_id = f.dwarf_id
        ),
        'squad_ids',(
            SELECT JSON_ARRAYAGG(w.squad_id)
            FROM squad_members w
            WHERE w.dwarf_id = f.dwarf_id
        ),
        'equipment_ids',(
            SELECT JSON_ARRAYAGG(s.equipment_id)
            FROM equipment s
            WHERE s.dwarf_id = f.dwarf_id
        )
    ) AS related_entities
    FROM dwarves f;
-- Задача 3: Данные о мастерской с назначенными рабочими и проектами
SELECT
    f.workshop_id,
    f.name,
    f.type,
    f.quality,
    JSON_OBJECT(
        'craftsdwarf_ids',(
            SELECT JSON_ARRAYAGG(d.dwarf_id)
            FROM workshop_craftsdwarves d
            WHERE d.workshop_id = f.workshop_id
        ),
        'project_ids',(
            SELECT JSON_ARRAYAGG(da.project_id)
            FROM projects da
            WHERE da.workshop_id = f.workshop_id
        ),
        'input_material_ids',(
            SELECT JSON_ARRAYAGG(w.material_id)
            FROM workshop_material w
            WHERE w.workshop_id = f.workshop_id
        ),
        'output_product_ids',(
            SELECT JSON_ARRAYAGG(s.product_id)
            FROM workshop_products s
            WHERE s.workshop_id = f.workshop_id
        )
    ) AS related_entities
    FROM workshops f



--Задача 4: Данные о военном отряде с составом и операциями