-- -- # Write your MySQL query statement below
-- -- -- select min(abs(a.x-b.x)) as shortest
-- -- -- from point a cross join point b
-- -- -- where a.x !=b.x
-- with base as 
-- (select 
-- lag(x) over(order by x asc) as prev,
-- x,
-- lead(x) over(order by x asc) as next
-- from Point
-- )
-- select 
-- case 
-- when prev is null then abs(x-(next))
-- when next is null then abs(x-(prev))
-- else abs(x-(next)) 
-- end as shortest
-- from base 
-- order by 1 
-- limit 1


-- -- -- select min(abs(a.x-b.x)) as "shortest" from Point a cross join Point b
-- -- -- on  a.x!=b.x
































with base as 
(select 
x,
lead(x) over(order by x) as nxt
from Point 
order by 1 asc
)

select 
abs(abs(x)-abs(nxt)) as shortest
from base 
where nxt is not null 
order by 1 asc
limit 1 





































-- -- select min(abs(a.x-b.x)) as 'shortest' from point a cross join point b on 
-- -- a.x!=b.x








-- select min(abs(a.x-b.x)) shortest from point a cross join point b on a.x!=b.x





-- select min(abs(b.x-a.x)) as shortest from Point a cross join point b on a.x!=b.x 



























