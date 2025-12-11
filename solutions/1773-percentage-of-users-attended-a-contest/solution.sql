# Write your MySQL query statement below
select R.contest_id , round(count(distinct U.user_id)*100/(select count(*) from Users),2) as percentage
from Users U
right join Register R
on U.user_id = R.user_id 
group by contest_id
order by percentage desc, R.contest_id asc
