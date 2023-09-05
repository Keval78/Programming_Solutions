SELECT
    DISTINCT candidate_id
FROM
    Candidates
LEFT JOIN
    Rounds USING (interview_id)
GROUP BY
    candidate_id
HAVING
    SUM(score) > 15 AND AVG(years_of_exp) >= 2;