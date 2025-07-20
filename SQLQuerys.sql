

Select Top 5 
		'Product Name' = P.Name,
		'Sum of Sales' = SUM(SOD.LineTotal)
from SalesOrderDetail SOD 
INNER JOIN Product P on SOD.ProductID = p.ProductID
GROUP BY P.Name
ORDER BY SUM(SOD.OrderQty) DESC



---------------- Q2 -----------------


SELECT 
	pc.Name,
	AVG(SOD.unitprice) 'Average Unit Price'
FROM ProductCategory PC
INNER JOIN ProductSubcategory PSC on psc.ProductCategoryID = pc.ProductCategoryID
INNER JOIN Product p on p.ProductSubcategoryID = PSC.ProductSubcategoryID
INNER JOIN SalesOrderDetail SOD on SOD.ProductID = p.ProductID
WHERE PC.Name in ('Bikes','Components')
GROUP BY PC.name





---------------- Q3 -----------------
SELECT 
	P.Name AS ProductName,
    SUM(SOD.OrderQty) AS 'Total Order Quantity'
FROM SalesOrderDetail sod
INNER JOIN Product p ON sod.ProductID = P.ProductID
INNER JOIN ProductSubcategory psc ON P.ProductSubcategoryID = PSC.ProductSubcategoryID
INNER JOIN ProductCategory pc ON PSC.ProductCategoryID = PC.ProductCategoryID
WHERE PC.Name NOT IN ('Clothing', 'Components')
GROUP BY P.Name




---------------- Q4 -----------------



SELECT 
	TOP 3 ST.Name,
	SUM(SOD.TotalDue) 'Sum of sales'
	FROM SalesTerritory ST
INNER JOIN SalesOrderHeader SOD ON ST.TerritoryID = SOD.TerritoryID
GROUP BY ST.Name
ORDER BY SUM(SOD.TotalDue) desc


---------------- Q5 -----------------

SELECT 
    C.CustomerID,
    Name = P.FirstName +' '+P.LastName
FROM Customer C
INNER JOIN Person P ON C.PersonID = P.BusinessEntityID
LEFT JOIN SalesOrderHeader SOH ON C.CustomerID = SOH.CustomerID
WHERE SOH.SalesOrderID IS NULL



---------------- Q6 -----------------


DELETE FROM SalesTerritory
WHERE TerritoryID NOT IN (
    SELECT DISTINCT TerritoryID 
    FROM SalesPerson
    WHERE TerritoryID IS NOT NULL
)





---------------- Q7 -----------------





INSERT INTO [dbo].[SalesTerritory]
           ([Name]
           ,[CountryRegionCode]
           ,[Group]
           ,[SalesYTD]
           ,[SalesLastYear]
           ,[CostYTD]
           ,[CostLastYear]
           ,[rowguid]
           ,[ModifiedDate])

SELECT      [Name]
           ,[CountryRegionCode]
           ,[Group]
           ,[SalesYTD]
           ,[SalesLastYear]
           ,[CostYTD]
           ,[CostLastYear]
           ,[rowguid]
           ,[ModifiedDate]

FROM [AdventureWorks2022].[Sales].[SalesTerritory] a
WHERE NOT EXISTS (
    SELECT TerritoryID 
    FROM  SalesTerritory b
    WHERE b.TerritoryID = a.TerritoryID
)







---------------- Q8 -----------------





SELECT 
   'Customer name' = p.FirstName + ' ' + p.LastName, 
    COUNT(SOH.SalesOrderID) OrderCount
FROM Customer c
INNER JOIN Person P ON C.PersonID = P.BusinessEntityID
INNER JOIN SalesOrderHeader SOH ON C.CustomerID = SOH.CustomerID
GROUP BY 
    p.FirstName, 
    p.LastName
HAVING 
    COUNT(soh.SalesOrderID) > 20


---------------- Q9 -----------------



SELECT GroupName, 
		COUNT(*) AS DepartmentAmount
FROM Department
GROUP BY GroupName
HAVING COUNT(*) > 2




---------------- Q10 -----------------


SELECT 'Emplpyee name' = P.FirstName +' ' + P.LastName,
    D.Name AS DepartmentName,
    S.Name AS ShiftName
FROM EmployeeDepartmentHistory EDH
INNER JOIN Department D ON EDH.DepartmentID = D.DepartmentID
INNER JOIN Shift S ON EDH.ShiftID = S.ShiftID
INNER JOIN Employee E ON EDH.BusinessEntityID = E.BusinessEntityID
INNER JOIN person P on P.BusinessEntityID = E.BusinessEntityID
WHERE 
    YEAR(EDH.StartDate) > 2010
    AND D.GroupName IN ('Manufacturing', 'Quality Assurance')


