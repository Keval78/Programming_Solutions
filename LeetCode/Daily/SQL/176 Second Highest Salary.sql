SELECT
    IFNULL(
        (SELECT DISTINCT Salary
         FROM Employee
         ORDER BY 1 DESC
         LIMIT 1, 1),
        NULL
    ) AS SecondHighestSalary;