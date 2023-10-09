-- Write your MySQL query statement below

SELECT
    dept_name,
    IFNULL(cnt, 0) AS student_number
FROM 
    Department LEFT JOIN
    (SELECT 
        dept_id, COUNT(student_id) as cnt
    FROM
        Student
    GROUP BY
        dept_id
    ) s USING(dept_id)
ORDER BY 2 DESC, 1 ASC;
