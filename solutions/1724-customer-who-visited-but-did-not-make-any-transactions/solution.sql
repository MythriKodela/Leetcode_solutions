# Write your MySQL query statement below
select V.customer_id, COUNT(V.visit_id) as count_no_trans 
from Visits V 
left join Transactions t on V.visit_id = t.visit_id 
where t.transaction_id is NULL
group by V.customer_id
