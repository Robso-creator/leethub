with tbl_rnk as (
    select
        num, id - row_number() over (partition by num order by id asc) as grp
    from logs
)
select distinct
    num "ConsecutiveNums"
from tbl_rnk
group by num, grp having count(grp) >= 3