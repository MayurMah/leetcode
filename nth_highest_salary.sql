CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
	Declare @NthHighestSalary INTEGER;
    SET @NthHighestSalary = NULL;
	IF @N <= (select count(*) from Employee)
		BEGIN	
			select @NthHighestSalary = Salary 
			from 
			(
				select *, DENSE_RANK() over(order by Salary desc) sal_rank from Employee
			) emp_ranked
			where sal_rank = @N
		END 	
	RETURN @NthHighestSalary;
END