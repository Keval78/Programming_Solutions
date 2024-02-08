SELECT
    (WEEK(purchase_date) - WEEK('2023-11-01') + 1) AS week_of_month,
    purchase_date,
    SUM(amount_spend) as total_amount
FROM
    (SELECT * FROM Purchases WHERE WEEKDAY(purchase_date) = 4) AS friday_purchases
GROUP BY
    week_of_month
ORDER BY 
    week_of_month;