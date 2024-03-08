SELECT
    item_type,
    CASE WHEN item_type = "prime_eligible" THEN FLOOR(500000/SUM(square_footage)) * COUNT(item_id)
    ELSE FLOOR((500000%(SELECT SUM(square_footage) FROM Inventory WHERE item_type = "prime_eligible"))/SUM(square_footage)) * COUNT(item_id)
    END as item_count
FROM Inventory
GROUP BY item_type
ORDER BY item_count DESC;