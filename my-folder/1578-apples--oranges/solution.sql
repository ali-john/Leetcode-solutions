# Write your MySQL query statement below

SELECT sale_date, SUM(
    CASE WHEN fruit in ('apples') THEN sold_num
         WHEN fruit in ('oranges') THEN (sold_num)*-1
         END
) as diff
FROM Sales s
GROUP BY sale_date
ORDER BY 1
