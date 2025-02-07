# Write your MySQL query statement below
SELECT Customers.name as 'Customers'from Customers
WHERE id NOT IN  (SELECT DISTINCT customerID from Orders);

