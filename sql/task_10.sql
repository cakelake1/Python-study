--11.5.1. Отберите с помощью LEFT JOIN все записи из таблицы Customers, для которых FK-ключ таблицы Orders пустой.

SELECT * FROM Customers 
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID 
WHERE Orders.CustomerID IS NULL

--11.5.2. Выведите конкретную информацию по всем пользователям Customers и поставщикам Suppliers -- имя контактной персоны, город и страну, а также идентификацию группы (пользователь или поставщик).

SELECT ContactName, City, Country,'Customer' As Type FROM Customers 
UNION
SELECT ContactName, City, Country,'Supplier' As Type FROM Suppliers 

