WITH diff_logs AS(
    SELECT 
        log_id, 
        log_id - ROW_NUMBER() OVER(ORDER BY log_id) AS diff
    FROM 
        Logs
)

SELECT 
    MIN(log_id) AS 'start_id', 
    MAX(log_id) AS 'end_id'
FROM
    diff_logs
GROUP BY
    diff;