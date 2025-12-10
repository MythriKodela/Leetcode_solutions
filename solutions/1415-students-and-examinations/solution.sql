# Write your MySQL query statement below
select S.student_id, S.student_name, SUB.subject_name, count(E.student_id) as attended_exams
from Students S
cross join Subjects SUB
left join Examinations E
on S.student_id = E.student_id and SUB.subject_name = E.subject_name
group by S.student_id , S.student_name, SUB.subject_name
Order by S.student_id , S.student_name, SUB.subject_name;
