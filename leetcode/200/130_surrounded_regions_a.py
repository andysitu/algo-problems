from typing import List

class Solution:
    def mark(self, board, y, x):
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
            return True
        if board[y][x] == 'X':
            return True
        if board[y][x] == 'A':
            return False

        board[y][x] = 'X'
        result = True
        if y == 0 or y == len(board) - 1:
            result = False
        elif x == 0 or x == len(board[0]) - 1:
            result = False
        
        if result:
            r1 = self.mark(board, y+1, x)
            r2 = self.mark(board, y-1, x)
            r3 = self.mark(board, y, x+1)
            r4 = self.mark(board, y, x-1)

            if r1 == False or r2 == False or r3 == False or r4 == False:
                result = False
        
        if result == False:
            board[y][x] = 'A'
        

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.mark(board, i, j)
        print(board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
        print(board)

s = Solution()
# s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# s.solve([["O","O","O"],["O","O","O"],["O","O","O"]])
s.solve([
    ["O","X","X","O","X"],
    ["X","O","O","X","O"],
    ["X","O","X","O","X"],
    ["O","X","O","O","O"],
    ["X","X","O","X","O"]])

[["O","X","X","O","X"],
["X","X","X","X","O"],
["X","X","X","X","X"],
["O","X","X","X","O"],
["X","X","O","X","O"]]