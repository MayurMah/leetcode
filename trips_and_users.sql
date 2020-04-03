/* Write your T-SQL query statement below */
-- Goal : Get cancellation rates for unbanned users (driver and cliet both) between Oct 1 & Oct 3 by date
-- Logic: 
-- a. Get unbanned users from Users table 
-- b. Get all trips between Oct 1 & Oct 3 inner joined on Client_Id & Driver_Id
-- c. Group by date, sum(trips) s1, sum(cancelled trips) s2, rate as s2/s1

select t.Request_at Day,round(cast(sum(case when t.Status in ('cancelled_by_client','cancelled_by_driver') then 1 else 0 end) as float)/count(*),2) as "Cancellation Rate" from Trips t 
join Users u1 on t.Client_Id = u1.Users_Id and u1.Banned = 'No'
join Users u2 on t.Driver_Id = u2.Users_Id and u2.Banned = 'No'
where t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at;