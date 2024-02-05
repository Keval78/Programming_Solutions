SELECT
    id,
    CASE WHEN p_id IS NULL THEN "Root"
    WHEN id IN (SELECT t.p_id FROM Tree t)THEN "Inner"
    ELSE "Leaf" END as type
FROM Tree;