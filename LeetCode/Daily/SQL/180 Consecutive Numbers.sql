SELECT 
  DISTINCT num as ConsecutiveNums
FROM(
  SELECT
    num,
    LAG(num, 1) OVER() as prev_num,
    LAG(num, 2) OVER() as prev2_num
  FROM
    Logs) T
WHERE num = prev_num AND num = prev2_num;