
-- Recursive Query in SQL
WITH RECURSIVE mng_hirerachy AS (
    SELECT *, 0 AS lvl 
    FROM Employees 
    WHERE employee_id = 1
    
    UNION
    
    SELECT E.*, M.lvl+1 AS lvl 
    FROM mng_hirerachy M JOIN Employees E ON M.employee_id = E.manager_id
    WHERE M.lvl < 3 AND E.employee_id != E.manager_id
)

SELECT distinct(employee_id) FROM mng_hirerachy WHERE lvl > 0;