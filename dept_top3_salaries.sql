/* Write your T-SQL query statement below */
-- Goal: Find employees with top three salaries in each department
-- Logic: Rank by salary within each department and chose rows where rank <= 3

select Department, Employee, Salary from 
(
	select d.Name as Department, e.Name as Employee, e.Salary , DENSE_RANK() over (partition by e.DepartmentId order by e.Salary desc) as sal_rank
	from Employee e join Department d 
	on e.DepartmentId = d.Id
) emp_ranked
where sal_rank <= 3