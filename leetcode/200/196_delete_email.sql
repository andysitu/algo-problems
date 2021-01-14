# Write your MySQL query statement below
DELETE p2 FROM PERSON p1
INNER JOIN
PERSON p2
ON p1.email = p2.email and p2.id > p1.id