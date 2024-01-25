SELECT
    class
FROM
    Courses
GROUP BY
    class
HAVING
    Count(student) >= 5;
