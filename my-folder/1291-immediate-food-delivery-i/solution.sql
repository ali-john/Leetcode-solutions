# Write your MySQL query statement below

SELECT round(100* AVG(order_date = customer_pref_delivery_date), 2
) as immediate_percentage
FROM Delivery


