# Write your MySQL query statement below
select product_name, year, price from Sales as S left join product as P on S.product_id = P.product_id
