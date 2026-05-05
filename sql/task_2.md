3.9. Задания
3.9.1. Напишите запрос, формирующий полный список товаров (Products) и выводящий название товара и количество единиц на складе.

SELECT ProductName, UnitsInStock FROM Products

3.9.2. Напишите запрос, формирующий список товаров (Products) и выводящий название товара и цену для тех товаров, которые дешевле 20.

SELECT * FROM Products
WHERE UnitPrice < 20

3.9.3. Выведите список заказов, у которых плата за доставку груза (Freight) лежит в диапазоне от 11.7 до 98.1.

SELECT * FROM Orders
WHERE (Freight >= 11.7) and (Freight <= 98.1)

3.9.4. Отберите всех сотрудников (Employees) - мужчин (анализируйте поле TitleOfCourtesy).

SELECT * FROM Employees
WHERE TitleOfCourtesy = 'Mr.'

3.9.5. Отберите всех поставщиков (Suppliers) из Японии.

SELECT * FROM Suppliers
WHERE Country = 'Japan'

3.9.6. Отберите все заказы, для которых идентификатор сотрудника-исполнителя равен 2, 4 или 8.

SELECT * FROM Orders
WHERE (EmployeeID = 2) or (EmployeeID =4) or (EmployeeID = 8)

3.9.7. Выведите идентификаторы заказов и товаров из таблицы Order Details, для которых цена больше 40, а количество (Quantity) меньше 10.

SELECT OrderID, ProductID FROM [Order Details]
WHERE (UnitPrice > 40) AND (Quantity < 10)