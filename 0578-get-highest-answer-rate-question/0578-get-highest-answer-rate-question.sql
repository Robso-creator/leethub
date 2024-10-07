-- Write your PostgreSQL query statement below

with tbl_rank as (
select
    question_id, 
    count(answer_id)::numeric / count(question_id) rate
from surveylog
group by question_id 
order by rate desc, question_id asc 
)
select 
    question_id as survey_log
from tbl_rank 
limit 1