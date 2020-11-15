# Write your MySQL query statement below
SELECT e1.NAME as `Employee` FROM EMPLOYEE as e1
INNER JOIN EMPLOYEE as e2
ON e1.ManagerId = e2.Id and e1.Salary > e2.Salary