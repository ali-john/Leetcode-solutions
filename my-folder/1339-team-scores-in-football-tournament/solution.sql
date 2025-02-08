# Write your MySQL query statement below


SELECT team_id, team_name, SUM(
    CASE WHEN team_id = host_team AND host_goals>guest_goals THEN 3
         WHEN team_id = guest_team AND guest_goals>host_goals THEN 3
         WHEN host_goals = guest_goals THEN 1 ELSE 0 
         END ) as num_points
FROM Teams T
LEFT JOIN Matches M ON T.team_id = M.host_team or T.team_id = M.guest_team
GROUP BY T.team_id
ORDER BY 3 DESC, 1 ASC;

