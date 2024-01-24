WITH CTE AS(
    SELECT
        name AS Employee,
        salary As Salary,
        MAX(salary) OVER(PARTITION BY departmentId) AS max_salary,
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
    Salary = max_salary;