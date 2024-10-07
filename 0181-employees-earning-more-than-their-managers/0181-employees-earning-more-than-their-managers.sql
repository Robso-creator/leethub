# Write your MySQL query statement below


select
    employee.name as Employee
from employee
left join employee as manager
    on manager.id = employee.managerid
where manager.salary < employee.salary