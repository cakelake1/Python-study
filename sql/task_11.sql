--12.3.1. Добавьте нового пользователя в таблицу Employees.

INSERT INTO Employees(LastName, FirstName,Title,TitleOfCourtesy,BirthDate, HireDate, Address, City, Country)
VALUES ('Doronin', 'Nickolay','Sales Manager', 'Mr.','19910510', '20120510', 'Georgia 1936', 'Zelenograd','RUS' )

--12.3.2. Свяжите этого нового пользователя с какой-либо территорией с помощью таблицы EmployeeTerritories (многие-ко-многим).

INSERT INTO EmployeeTerritories(EmployeeID, TerritoryID)
VALUES (12, '125007' )

--12.3.3. Попробуйте добавить новую запись в таблицу заказов Orders. Возникнут ли какие-либо конфликты?

INSERT INTO Orders(EmployeeID)
VALUES (12)
-- Если я добавляю запись с реальным сотрудником, то кофликтов нет, если добавляю с несуществующим, то возникает конфликт по FK(EmployeeID)
