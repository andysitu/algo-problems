# Write your MySQL query statement below
SELECT w2.id FROM WEATHER W1, WEATHER W2
WHERE (DATEDIFF(w2.recorddate, w1.recorddate) = 1)
AND W2.TEMPERATURE > W1.TEMPERATURE