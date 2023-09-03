-- # SELECT id
-- # previousday temprature < currentday temprature

-- # Solve it using Self JOIN
SELECT 
    w2.id
FROM 
    Weather w1 
    INNER JOIN 
    Weather w2 
ON 
    w1.recordDate = w2.recordDate - 1 
    AND 
    w1.temperature < w2.temperature;


-- # Solve it using Window Function LAG
WITH 
    Weather_diff 
AS(
    SELECT 
        id, 
        temperature - LAG(temperature) OVER(ORDER BY recordDate) AS temp_diff,
        DATEDIFF(recordDate, LAG(recordDate) OVER(ORDER BY recordDate)) AS date_diff
    FROM 
        Weather
)

SELECT 
    id
FROM
    Weather_diff
WHERE 
    temp_diff>0 AND date_diff = 1;