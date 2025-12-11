SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM visits 
left join Transactions
ON visits.visit_id = Transactions.visit_id
where Transactions.visit_id IS NULL
GROUP BY customer_id

