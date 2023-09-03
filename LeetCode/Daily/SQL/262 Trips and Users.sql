
-- query using exists
WITH
Unbanned_Trips AS(
    SELECT
    *
    FROM
    Trips T
    WHERE
    T.request_at  BETWEEN '2013-10-01' AND '2013-10-03'
    AND
    EXISTS(
        SELECT 1
        FROM USERS U
        WHERE U.banned='No'
        AND T.client_id=U.users_id
    )
    AND
    EXISTS(
        SELECT 1
        FROM USERS U
        WHERE U.banned='No'
        AND T.driver_id=U.users_id
    )
),

total_requests AS(
    SELECT request_at, Count(*) AS no_requests
    FROM Unbanned_Trips
    GROUP BY T.request_at
),

total_cancels AS(
    SELECT request_at, Count(*) AS no_cancels
    FROM Unbanned_Trips
    WHERE status in ('cancelled_by_driver', 'cancelled_by_client')
    GROUP BY T.request_at
)

SELECT
    TR.request_at AS 'Day',
    ROUND(COALESCE(TC.no_cancels, 0)/TR.no_requests, 2) AS 'Cancellation Rate'
FROM
    total_requests TR LEFT JOIN total_cancels TC
    ON TR.request_at = TC.request_at



-- short query using join
WITH 
    Unbanned_Trips AS(
    SELECT
        T.*
    FROM
        Trips T 
        LEFT JOIN Users AS Clients ON T.client_id = Clients.users_id 
        LEFT JOIN Users AS Drivers ON T.driver_id = Drivers.users_id 
    WHERE 
        T.request_at  BETWEEN '2013-10-01' AND '2013-10-03'
        AND Clients.banned = 'No'
        AND Drivers.banned = 'No'
    )

SELECT 
    request_at AS 'Day', 
    ROUND(SUM(status != "completed")/Count(*), 2) AS 'Cancellation Rate'
FROM  
    Unbanned_Trips
GROUP BY 
    request_at
ORDER BY
    request_at;