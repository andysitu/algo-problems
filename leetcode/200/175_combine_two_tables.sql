# Write your MySQL query statement below
SELECT p.FirstName, p.LastName, adr.City, adr.State 
from Person as p
LEFT JOIN Address as adr
ON p.PersonId = adr.PersonId;