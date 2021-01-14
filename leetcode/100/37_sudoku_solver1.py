class Solution:
    solved = -1
    def build_table(self, board):
        self.solved = 0
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    board[row][col] = {
                        "length": 9,
                        "nums": [1] * 9
                    }
                else:
                    board[row][col] = int(board[row][col])
                    self.solved += 1
    
    def remove_row(self, board, num, row_index):
        row = board[row_index]
        for i in range(9):
            if type(row[i]) != int:
                nums = row[i]["nums"]
                
                if nums[num - 1]==1:
                    nums[num-1] = 0
                    row[i]["length"] -= 1
                    if row[i]["length"] <= 1:
                        row[i] = num
                        self.solved += 1

    def remove_col(self, board, num, col_index):
        for i in range(9):
            col = board[i][col_index]
            if type(col) != int:
                nums = col["nums"]
                
                if nums[num - 1]== 1:
                    nums[num-1] = 0
                    col["length"] -= 1
                    if col["length"] <= 1:
                        board[i][col_index] = num
                        self.solved += 1
    
    def remove_box(self, board, num, row_index, col_index):
        start_row = int(row_index / 3) * 3
        start_col = int(col_index / 3) * 3
        for i in range(3):
            for j in range(3):
                col = board[start_row + i][start_col + j]
                if type(col) != int:
                    nums = col["nums"]
                    
                    if nums[num - 1]== 1:
                        nums[num-1] = 0
                        col["length"] -= 1
                        if col["length"] <= 1:
                            board[start_row + i][start_col + j] = num
                            self.solved += 1

    def check_box(self, board, row, col):
        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3
        for num in range(1, 10):
            count = 0
            found = False
            last_row = -1
            last_col = -1
            for i in range(3):
                for j in range(3):
                    col = board[start_row + i][start_col + j]
                    if type(col) != int:
                        nums = col["nums"]
                        
                        if nums[num - 1] == 1:
                            last_row = start_row + i
                            last_col = start_col + j
                            count += 1
                    else:
                        if col == num:
                            found = True
            if count == 1 and found == False:
                board[last_row][last_col] = num
                self.solved += 1
                            
    
    def print_table(self, board):
        print(self.solved)
        for i in range(9):
            print("ROW :", i)
            print(board[i])

    def solveSudoku(self, board):
        self.build_table(board)
        while self.solved < 81:
            for row in range(9):
                for col in range(9):
                    n = board[row][col]
                    if type(n) != int:
                        continue
                    self.remove_box(board, n, row, col)
                    self.remove_row(board, n, row)
                    self.remove_col(board, n, col)
            self.print_table(board)
            for i in range(3):
                for j in range(3):
                    self.check_box(board, i * 3, j * 3)
        # for row in range(9):
        #     for col in range(9):
        #         board[row][col] = str(board[row][col])
        

s = Solution()
print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))