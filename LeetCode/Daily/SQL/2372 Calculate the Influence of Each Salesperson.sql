SELECT 
    Sp.salesperson_id, 
    Sp.name, 
    SUM(COALESCE(S.price, 0)) AS total
FROM
    Salesperson Sp 
LEFT JOIN 
    Customer Cm 
    ON Sp.salesperson_id = Cm.salesperson_id
LEFT JOIN 
    Sales S
    ON Cm.customer_id = S.customer_id
GROUP BY 
    Sp.salesperson_id;