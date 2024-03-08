WITH CTE AS(
    SELECT ROW_NUMBER() OVER(ORDER BY topping_name ASC) as rnk, topping_name, cost FROM Toppings
)

SELECT
    CONCAT(t1.topping_name, ",", t2.topping_name, ",", t3.topping_name) as pizza, ROUND(t1.cost + t2.cost + t3.cost, 2) as total_cost
FROM
    CTE as t1 
    JOIN 
    CTE as t2 
    ON t1.rnk < t2.rnk
    JOIN 
    CTE as t3 
    ON t2.rnk < t3.rnk
ORDER BY 
    2 DESC, 1 ASC;
