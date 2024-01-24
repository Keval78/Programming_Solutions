SELECT
    Email
FROM
    Person
GROUP BY 
    email
HAVING
    count(id) > 1;
    