
-- Using Self join
SELECT
    T1.account_id,
    T1.day,
    SUM(
        CASE WHEN T2.type="Deposit" THEN T2.AMOUNT
        ELSE -T2.AMOUNT END
    ) AS balance
FROM 
    Transactions T1
    JOIN Transactions T2
    ON T1.account_id = T2.account_id AND T1.day >= T2.day
GROUP BY 
    1, 2
ORDER BY 
    1, 2;


-- Using Window Function.
SELECT
    account_id, 
    day,
    SUM(
        CASE WHEN type="Deposit" THEN AMOUNT
        ELSE -AMOUNT END
    ) OVER(PARTITION BY account_id ORDER BY day) as balance
FROM 
    Transactions;