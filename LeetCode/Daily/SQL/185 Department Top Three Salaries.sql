WITH CTE AS(
    SELECT
        name AS Employee,
        salary As Salary,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY SALARY DESC) AS salary_rank,
        departmentId
    FROM
        Employee
)

SELECT
    name as Department,
    Employee,
    Salary
FROM
    CTE LEFT JOIN Department ON departmentId = id
WHERE
    salary_rank < 4;