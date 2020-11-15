class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return board
        rows = len(board)
        cols = len(board[0])
        
        
        for i in range(rows):
            for j in range(cols):
                numlive = 0
                if j < cols-1:
                    if board[i][j+1] > 0:
                        numlive += 1
                    if i < rows-1 and board[i+1][j+1] > 0:
                        numlive += 1
                    if i > 0 and board[i-1][j+1] > 0:
                        numlive += 1
                if j > 0:
                    if board[i][j-1] > 0:
                        numlive += 1
                    if i < rows-1 and board[i+1][j-1] > 0:
                        numlive += 1
                    if i > 0 and board[i-1][j-1] > 0:
                        numlive += 1
                if i > 0 and board[i-1][j] > 0:
                    numlive += 1
                if i < rows-1 and  board[i+1][j] > 0:
                    numlive += 1
                    
                if board[i][j]  == 1:
                    if numlive > 3 or numlive < 2:
                        board[i][j] = 2
                else:
                    if numlive == 3:
                        board[i][j] = -1
                        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1