SELECT
    id, visit_date, people
FROM(
    SELECT
        id, visit_date, people,
        LEAD(people) OVER w as next_people, 
        LEAD(people, 2) OVER w as next2_people, 
        LAG(people) OVER w as prev_people,
        LAG(people, 2) OVER w as prev2_people
    FROM
        Stadium
    WINDOW w AS (ORDER BY id)
) as cte
WHERE
    (people>99 AND next_people>99 AND next2_people>99)
    OR (prev_people>99 AND people>99 AND next_people>99)
    OR (prev2_people>99 AND prev_people>99 AND people>99);
