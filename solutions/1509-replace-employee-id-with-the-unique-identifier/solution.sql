# Write your MySQL query statement below
select unique_id, name from Employees as E left join EmployeeUNI as AU on E.id = AU.id 

