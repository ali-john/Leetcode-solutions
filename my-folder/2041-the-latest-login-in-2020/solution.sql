# Write your MySQL query statement below

SELECT user_id, MAX(time_stamp) as last_stamp
FROM Logins l
WHERE Year(time_stamp) = 2020
GROUP BY user_id
ORDER BY time_stamp DESC
