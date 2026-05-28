--Задание. Добавьте подходящие индексы для таблиц тестовой базы, созданной в предыдущем занятии.
CREATE CLUSTERED INDEX idxRegion_RegionID ON Region(RegionID)
CREATE CLUSTERED INDEX idxTerritories_TerritoryID ON Territories(TerritoryID)
CREATE INDEX idxTerritories_RegionID ON Territories(RegionID)