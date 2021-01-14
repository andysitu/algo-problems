from typing import List

class Solution:
    def mark(self, board, y, x):
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
            return True
        if board[y][x] != 'O':
            return True

        board[y][x] = 'A'
        
        self.mark(board, y+1, x)
        self.mark(board, y-1, x)
        self.mark(board, y, x+1)
        self.mark(board, y, x-1)
            
    def print_board(self, board):
        for i in range(len(board)):
            print(board[i])
       
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        for i in range(len(board)):
            if board[i][0] == 'O':
                self.mark(board,i,0)
            if board[i][len(board[0]) - 1] == 'O':
                self.mark(board,i,len(board[0]) - 1)
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.mark(board,0,i)
            if board[len(board) - 1][i] == 'O':
                self.mark(board,len(board)-1,i)
        # self.print_board(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        self.print_board(board)

s = Solution()
# s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# s.solve([["O","O","O"],["O","O","O"],["O","O","O"]])
s.solve([
    ["X","O","X","O","X"],
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

[["O","X","X","O","X"],
["X","O","O","X","O"],
["X","O","X","O","X"],
["O","X","O","O","O"],
["X","X","O","X","O"]]