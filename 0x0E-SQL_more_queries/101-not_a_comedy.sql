-- lists all shows without the genre Comedy in the database
SELECT DISTINCT `title`
FROM `tv_shows` AS ts LEFT JOIN `tv_shows_genres` AS tsg ON tsg.`show_id` = ts.`id`
LEFT JOIN `tv_genres` AS tg ON tg.`id` = ts.`genre_id` WHERE tg.`title` NOT IN
(SELECT `title` FROM `tv_shows` AS ts INNER JOIN `tv_show_genres` AS tsg ON tsg.`show_id` = ts.`id INNER JOIN `tv_genres` AS tg ON tg.`id` = ts.`genre_id` WHERE tg.`name` = "Comedy") ORDER BY `title`;
