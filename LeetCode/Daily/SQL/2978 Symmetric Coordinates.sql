SELECT 
    X, Y 
FROM 
    (
        SELECT 
            DISTINCT c1.X, c1.Y 
        FROM 
            Coordinates c1 
            JOIN Coordinates c2 ON (c1.X = c2.Y) 
            AND (c2.X = c1.Y) 
        WHERE 
            c1.X < c1.Y 
        UNION 
        SELECT 
            X, Y 
        FROM 
            coordinates 
        WHERE 
            X = Y 
        GROUP BY 
            X 
        HAVING 
            count(X) > 1
    ) as t 
ORDER BY 
    1, 2;