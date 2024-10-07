-- Write your PostgreSQL query statement below
select 
    question_id as survey_log
    from (
select
    question_id, 
    count(answer_id)::numeric / count(question_id) rate
from surveylog
group by question_id 
order by rate desc, question_id asc limit 1
)