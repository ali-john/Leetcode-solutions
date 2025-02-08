# Write your MySQL query statement below

SELECT player_id, MIN(event_date) as first_login
FROM Activity a
GROUP BY player_id
