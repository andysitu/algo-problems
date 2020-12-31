"""
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. The 
same letter cell may not be used more than once.
"""

"""
Brute Force
Search for all the cells individual and then see if it matches char by char
O(n^2 * l)
"""

"""
DFS Recursion
In Looking at the brute force approach, it would use BFS or DFS to search
for all the combinations. In this case, it would be easier to code for DFS
and and recursion which will also backtrack to search other possibilities
(using the four directions). 
"""