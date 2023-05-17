#!/usr/bin/env bash
-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
LEFT JOIN (
    SELECT m.genre_id
    FROM tv_show_genres m
    INNER JOIN tv_shows s ON m.show_id = s.id
    WHERE s.title = 'Dexter'
) AS m
ON g.id = m.genre_id
WHERE m.genre_id IS NULL
ORDER BY g.name ASC;
