-- Lists all cities in the database hbtn_0d_usa in an ascending order by cities.id
-- Each record displays cities.id - cities.name - states.name
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
