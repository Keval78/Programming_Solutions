SELECT 
    question_id as survey_log
FROM
    SurveyLog
GROUP BY
    question_id
ORDER BY
    COUNT(CASE WHEN action = 'answer' THEN question_id ELSE NULL END) / COUNT(CASE WHEN action = 'show' THEN question_id ELSE NULL END) DESC, 1
LIMIT 1;