# Write your MySQL query statement below
SELECT S.Score, (
    SELECT COUNT(Distinct Score) FROM Scores WHERE Score >= S.Score) As `Rank`
FROM Scores S
ORDER BY S.Score DESC;