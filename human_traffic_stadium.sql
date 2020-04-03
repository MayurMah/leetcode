/* Write your T-SQL query statement below */
-- Goal: Display records with >= 3 consecutive rows and people >= 100
-- Logic: 
-- Group consecutive records with people >= 100 and show records where number of consecutive records >= 3

-- version 1 with CTE ---
/*With stadium_diff as 
(
select *, (id-ROW_NUMBER() over (order by id)) diff from stadium 
where people >= 100
),
stadium_diff_count as 
(
select *, count(*) over(partition by diff) as diffcount from stadium_diff
)
select id,visit_date,people from stadium_diff_count
where diffcount >= 3*/

-- version 2 without CTE --
select id,visit_date,people from
	(
	select *, count(*) over(partition by diff) as diffcount from 
		(
			select *, (id-ROW_NUMBER() over (order by id)) diff from stadium 
			where people >= 100
		) stadium_diff
	) stadium_diff_count
where diffcount >= 3

-- version 3 ---
/*select distinct s1.* 
from stadium s1, stadium s2, stadium s3 
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100 and 
(
	(s1.id = s2.id-1 and s1.id = s3.id-2)
	OR
	(s2.id = s1.id-1 and s2.id = s3.id-2)
	OR
	(s2.id = s3.id-1 and s2.id = s1.id-2)
)*/