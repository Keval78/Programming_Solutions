SELECT
    stock_name,
    sum(
        CASE WHEN operation='Buy' THEN(-1)*price
        ELSE price
        END
    ) as 'capital_gain_loss'
FROM 
    Stocks
GROUP BY 
    stock_name;
