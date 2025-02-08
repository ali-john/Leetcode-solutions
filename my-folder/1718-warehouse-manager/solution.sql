# Write your MySQL query statement below

SELECT name as warehouse_name, SUM(
    Width*Length*Height * units
) as volume
FROM Warehouse W
LEFT JOIN Products P ON W.product_id = P.product_id
GROUP BY name
