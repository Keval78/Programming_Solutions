
SELECT
    product_id, product_name
FROM
    Sales LEFT JOIN Product USING (product_id)
GROUP BY product_id
HAVING 
    MIN(sale_date) >= '2019-01-01' 
    AND 
    MAX(sale_date) <= '2019-03-31';


SELECT DISTINCT product_id, product_name
FROM Sales LEFT JOIN Product USING (product_id)
WHERE product_id NOT IN (
        SELECT DISTINCT product_id 
        FROM Sales 
        WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31');

