SELECT
    name as Customers
FROM
    Customers
WHERE
    id NOT IN (SELECT distinct(customerId) FROM Orders);