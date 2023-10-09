-- Write your MySQL query statement below

SELECT name
FROM (
        Select Count(id) as vote_cnt, candidateId
        FROM Vote
        Group BY candidateId 
        ORDER BY vote_cnt DESC 
        LIMIT 1
    ) v 
LEFT JOIN Candidate c ON v.candidateId = c.id;