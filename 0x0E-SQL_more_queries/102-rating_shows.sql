-- lists all shows by their rating

SELECT `title`, SUM(`rate`) AS `rating` FROM `tv_shows` AS ts INNER JOIN `tv_show_ratings` AS tsr ON ts.`id` = tsr.`show_id` GROUP BY `title` ORDER BY `rating` DESC;
