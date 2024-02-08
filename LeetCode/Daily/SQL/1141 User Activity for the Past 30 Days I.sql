SELECT
    activity_date as `day`, count(distinct user_id) as active_users
FROM
    Activity
Group BY
    `day`
HAVING
    `day` <= '2019-07-27' AND `day` > DATE_ADD('2019-07-27', INTERVAL -30 DAY);



-- DATEDIFF('2019-07-27', `day`)<30 AND DATEDIFF('2019-07-27', `day`)>=0 

-- DATEDIFF('2019-07-27', `day`) BETWEEN 0 AND 29

-- `day` BETWEEN date_sub('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
-- `day` BETWEEN DATE_ADD('2019-07-27', INTERVAL -29 DAY) AND '2019-07-27';

