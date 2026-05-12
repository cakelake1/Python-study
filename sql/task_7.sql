--8.3.1. Сформируйте список названий товаров (таблица Products) с указанием для каждого из них соответствующей категории (таблица Categories).

SELECT Categories.CategoryName, Products.ProductName FROM Categories, Products
WHERE Categories.CategoryID = Products.CategoryID

--8.3.2. Организуйте эквисоединение, которое выводит цену и названия тех товаров, для которых цена за единицу (UnitPrice) в таблице Order Details меньше 20.

SELECT Products.ProductName, [Order Details].UnitPrice FROM [Order Details], Products
WHERE [Order Details].ProductID = Products.ProductID
AND [Order Details].UnitPrice < 20

--8.3.3. Добавьте к предыдущему запросу третью таблицу Categories, и выведите в дополнение к названию товара его категорию.

SELECT Categories.CategoryName,Products.ProductName, [Order Details].UnitPrice FROM [Order Details], Products, Categories
WHERE [Order Details].ProductID = Products.ProductID
AND Categories.CategoryID = Products.CategoryID 
AND [Order Details].UnitPrice < 20