--1. Получить информацию о всех гномах, которые входят в какой-либо отряд, вместе с информацией об их отрядах.
SELECT *  FROM Dwarves, Squads
WHERE Dwarves.squad_id = Squads.squad_id 

--2. Найти всех гномов с профессией "miner", которые не состоят ни в одном отряде.

SELECT * FROM Dwarves
WHERE Dwarves.profession = 'miner'
AND squad_id IS NULL

--3. Получить все задачи с наивысшим приоритетом, которые находятся в статусе "pending".

SELECT * FORM Tasks
WHERE status = 'pending'
AND priority = (SELECT MAX(priority) FROM Tasks)

--4. Для каждого гнома, который владеет хотя бы одним предметом, получить количество предметов, которыми он владеет.

SELECT Dwarves.name, COUNT(Items.item_id) AS item_count FROM Dwarves
INNER JOIN Items ON Dwarves.dwarf_id = Items.owner_id
GROUP BY Dwarves.name

--5. Получить список всех отрядов и количество гномов в каждом отряде. Также включите в выдачу отряды без гномов.

SELECT squad_id, name, COUNT(Dwarves.dwarf_id) as dwarf_count FROM Squads
LEFT JOIN Dwarves on Squads.squad_id = Dwarves.squad_id
GROUP BY squad_id, name

--6. Получить список профессий с наибольшим количеством незавершённых задач ("pending" и "in_progress") у гномов этих профессий.

SELECT Dwarves.profession, COUNT(*) AS unfinished FROM Dwarves
INNER JOIN Tasks ON Dwarves.dwarf_id = Tasks.assigned_to
WHERE Tasks.status IN ('pending','in_progress')
GROUP BY Dwarves.profession
ORDER BY unfinished DESC

--7. Для каждого типа предметов узнать средний возраст гномов, владеющих этими предметами.

SELECT Items.Type, AVG(Dwarves.age) as avg_age from Items
INNER JOIN Dwarves ON Dwarves.dwarf_id = Items.owner_id
GROUP BY Items.Type 

--8. Найти всех гномов старше среднего возраста (по всем гномам в базе), которые не владеют никакими предметами.

SELECT * FROM Dwarves
LEFT JOIN Items ON Dwarves.dwarf_id = Items.owner_id
WHERE Dwarves.age > (SELECT AVG(age) FROM Dwarves) 
AND Items.owner_id IS NULL
