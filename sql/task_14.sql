--15.7. Задание
--Создайте в новой базе таблицу Territories со структурой, аналогичной структуре таблицы Territories из учебной базы. Добавьте в неё и таблицу Region несколько значений так, чтобы они оказались связаны друг с другом через FK.
-- Создаю Territories :
CREATE TABLE Territories ( 
    TerritoryID int NOT NULL, 
    TerritoryDescription nchar(30) NOT NULL, RegionID int NOT NULL );
--Добавляю несколько значений в поля:
INSERT INTO Region(RegionID, RegionDescription)
VALUES ('1', 'Eastern'),
('2','Western'),
('3','North'),
('4','SOUTH')
--и в Territories:
INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID)
VALUES    ('00001', 'Piter', 1),
('00002', 'Minsk', 1),
('00003', 'Moscow', 2),
('00004', 'Tver', 2),
('11115', 'Zelenograd', 3);
--Проверяем, что связь по первичному ключу работает:
SELECT t1.TerritoryID, t1.TerritoryDescription, t2.RegionID, t2.RegionDescription FROM Territories t1
JOIN Region t2 ON t1.RegionID = t2.RegionID
-- результат отрицательный, добавляем отдельно первичный ключ:
ALTER TABLE Region
ADD PRIMARY KEY (RegionID)
-- и
ALTER TABLE Territories
ADD PRIMARY KEY (TerritoryID, RegionID)
-- Проверка по первичному ключу проходит, задание выполнено


