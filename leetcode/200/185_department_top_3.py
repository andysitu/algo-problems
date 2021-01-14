SELECT D.NAME AS `Department`, E.NAME as `Employee`, E.SALARY as `Salary`
FROM
(select departmentid, salary, row_number() over(partition by departmentid order by salary desc) as rn
from (SELECT DISTINCT DEPARTMENTID, SALARY FROM EMPLOYEE) E) G
INNER JOIN EMPLOYEE AS E
ON E.SALARY = G.SALARY AND E.DEPARTMENTID = G.DEPARTMENTID
INNER JOIN DEPARTMENT AS D
ON E.DEPARTMENTID = D.ID
WHERE RN <= 3