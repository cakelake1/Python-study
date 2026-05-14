--10.4.1. Перепишите задание 8.3.2 через синтаксис JOIN.

SELECT Products.ProductName, [Order Details].UnitPrice FROM [Order Details]
JOIN Products ON [Order Details].ProductID = Products.ProductID
AND [Order Details].UnitPrice < 20

--10.4.2. Имеется запрос
--Проверьте этот запрос с вариантом FULL JOIN -- за счёт чего выдача получилась объёмнее? Почему значения NULL встречаются в обоих полях набора?
--Выдача стала больше, потому что FULL JOIN добавляет все строки и Заказов, без совпадений по Заказчикам и Берет строки по Заказчикам, без совпадений по заказам.

--10.4.3. Подумайте, как с помощью предложения WHERE превратить запрос CROSS JOIN в INNER JOIN.

SELECT Employees.FirstName, Employees.LastName, Orders.Freight
FROM Employees CROSS JOIN Orders
WHERE Employees.EmployeeID = Orders.EmployeeID

--10.4.4. Перепишите данный запрос в INNER JOIN:

SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products
INNER JOIN [Order Details] ON Products.ProductID = [Order Details].ProductID