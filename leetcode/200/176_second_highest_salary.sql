# Write your MySQL query statement below
Select (
    SELECT DISTINCT Salary 
    From Employee
    Order by Salary
    DESC LIMIT 1 OFFSET 1
 ) as "SecondHighestSalary";