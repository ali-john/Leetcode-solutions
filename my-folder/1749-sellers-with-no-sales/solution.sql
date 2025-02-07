# Write your MySQL query statement below
SELECT Seller.seller_name 
FROM Seller
where Seller.seller_id NOT IN 
(
    SELECT seller_id
    FROM Orders
    GROUP BY seller_id, sale_date
    HAVING sale_date >= '2020-01-01'
)
ORDER BY seller_name
