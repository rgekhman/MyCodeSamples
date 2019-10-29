--
-- Roman Gekhman - 
-- Galvanize Coding Exercise 6/26/18
-- roman.gekhman@gmail.com
-- 
-- Description: 
-- Write a SQL query that retrieves the names of all salespeople 
-- that have more than $1300 in orders from the tables above. 
-- You can assume that each salesperson only has one ID.
-- 
-- Output: 
-- Bob
-- Dan
-- Ken
--
SELECT Name 
FROM Salesperson s 
INNER JOIN 
( SELECT salesperson_id, "SUM" = Sum(amount) 
FROM Orders o 
GROUP BY o.salesperson_id 
HAVING Sum(amount) > 1300) x1 
ON s.ID = x1.salesperson_id