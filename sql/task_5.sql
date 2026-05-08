--6.3. Задания

--6.3.1. Выполните агрегацию таблицы Contacts по полю ContactType.

SELECT ContactType, 
COUNT(*) AS ContactCount
FROM Contacts
GROUP BY ContactType

--6.3.2. Выведите средние цены товаров (UnitPrice) в каждой из категорий (CategoryId) таблицы Products, отсортированные по возрастанию.

SELECT CategoryID, 
AVG(UnitPrice) AS AVGPrice
FROM Products
GROUP BY CategoryID
ORDER BY AVGPrice
