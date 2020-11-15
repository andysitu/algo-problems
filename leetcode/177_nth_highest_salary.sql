CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE p INT;
  SET p = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      Select (
        SELECT DISTINCT Salary 
        From Employee
        Order by Salary
        DESC LIMIT 1 OFFSET p
     )
  );
END