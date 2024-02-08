SELECT
    user_id as buyer_id,
    join_date,
    count(order_id) as orders_in_2019
FROM
    Users LEFT JOIN Orders ON Users.user_id = Orders.buyer_id AND YEAR(order_date) = 2019    
GROUP BY 1
ORDER BY 1;