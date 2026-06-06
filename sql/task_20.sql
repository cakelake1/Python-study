

--1. Найдите все отряды, у которых нет лидера.

SELECT name FROM Squads
WHERE leader_id is NULL

--2. Получите список всех гномов старше 150 лет, у которых профессия "Warrior".

SELECT name FROM Dwarves
WHERE age > 150
AND profession = 'Warrior'

--3. Найдите гномов, у которых есть хотя бы один предмет типа "weapon".

SELECT DISTINCT name FROM Dwarves
JOIN Items ON Dwarves.dwarf_id = Items.owner_id
WHERE Items.type = 'weapon'
--4. Получите количество задач для каждого гнома, сгруппировав их по статусу.
SELECT assigned_to, status, COUNT(*) AS task_number FROM Tasks
WHERE assigned_to IS NOT NULL
GROUP BY assigned_to, status
ORDER BY assigned_to, status

--5. Найдите все задачи, которые были назначены гномам из отряда с именем "Guardians".

SELECT * FROM Tasks
JOIN Dwarves ON Tasks.assigned_to = Dwarves.dwarf_id
WHERE Dwarves.squad_id IN (SELECT squad_id FROM Squads WHERE name = 'Guardians') 


--6. Выведите всех гномов и их ближайших родственников, указав тип родственных отношений.

SELECT d1.name AS Dwarfname, d2.name AS Relativename, r.relationship FROM Relationsips r
JOIN Dwarves d1 ON r.dwarf_id = d1.dwarf_id
JOIN Dwarves d2 ON r.related_to = d2.dwarf_id 