class Solution:
    solved = -1
    def eliminate_row(self, board, number, row):
        for j in range(9):
            t = board[row][j]
            if (type(t) == dict):
                if t["possible_numbers"][number - 1] == 1:
                    t["possible_numbers"][number - 1] = 0
                    t["numbers_left"] -= 1
    
    def eliminate_col(self, board, number, col):
        for j in range(9):
            t = board[j][col]
            if (type(t) == dict):
                if t["possible_numbers"][number - 1] == 1:
                    t["possible_numbers"][number - 1] = 0
                    t["numbers_left"] -= 1
    
    def eliminate_box(self, board, number, row, col):
        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3
        
        for r in range(3):
            for c in range(3):
                t = board[start_row + r][start_col + c]
                if (type(t) == dict):
                    if t["possible_numbers"][number - 1] == 1:
                        t["possible_numbers"][number - 1] = 0
                        t["numbers_left"] -= 1

    def solve_cell(self, board, number, row, col):
        self.solved += 1
        board[row][col] = str(number)
        self.eliminate_row(board, number, row)
        self.eliminate_col(board, number, col)
        self.eliminate_box(board, number, row, col)

    def check_box(self, board, row, col):
        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3
        for n in range(1, 10):
            found = False
            count = 0
            last_col = -1
            last_row = -1
            for r in range(3):
                for c in range(3):
                    t = board[start_row + r][start_col + c]
                    if (type(t) == dict):
                        if t["possible_numbers"][n - 1] == 1:
                            count += 1
                            last_col = start_col + c
                            last_row = start_row + r
                    else:
                        if int(t) == n:
                            found = True
                            break
                if found:
                    break
            if count == 1 and not found:
                self.solve_cell(board, n, last_row, last_col)

    
    
    def check_row(self, board, row):
        for n in range(1, 10):
            found = False
            count = 0
            last_col = -1
            for c in range(9):
                t = board[row][c]
                if (type(t) == dict):
                    if t["possible_numbers"][n - 1] == 1:
                        count += 1
                        last_col = c
                else:
                    if int(t) == n:
                        found = True
                        break
            if count == 1 and not found:
                self.solve_cell(board, n, row, last_col)

    def check_col(self, board, col):
        for n in range(1, 10):
            found = False
            count = 0
            last_row = -1
            for r in range(9):
                t = board[r][col]
                if (type(t) == dict):
                    if t["possible_numbers"][n - 1] == 1:
                        count += 1
                        last_row = r
                else:
                    if int(t) == n:
                        found = True
                        break
            if count == 1 and not found:
                self.solve_cell(board, n, last_row, col)

    def find_empty(self, board):
        for row in range(9):
            for col in range(9):
                if type(board[row][col]) != str:
                    return row, col
        return -1, -1

    def check_valid_number(self, board, num, row, col):
        n = str(num)
        for i in range(9):
            if board[row][i] == n:
                return False
            if board[i][col] == n:
                return False

        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3
        for r in range(3):
            for c in range(3):
                if board[start_row + r][start_col + c] == n:
                    return False
        return True

    def solve(self, board):
        r, c = self.find_empty(board)
        if r == -1:
            return True

        cell = board[r][c]
        numbers = cell["possible_numbers"]
        for i in range(9):
            if numbers[i] == 1:
                if self.check_valid_number(board, i+1, r, c):
                    board[r][c] = str(i+1)
                    if self.solve(board):
                        return True
                    board[r][c] = cell
        return False

    def solveSudoku(self, board):
        self.solved = 0
        # Modify board
        for row in range(9):
            for col in range(9):
                c = board[row][col]
                if c == ".":
                    board[row][col] = {
                        "possible_numbers": [1] * 9,
                        "numbers_left": 9
                    }
                else:
                    self.solved += 1

        # Navigate Rows, Eliminate Possibilities
        for row in range(9):
            for col in range(9):
                c = board[row][col]
                if type(c) == str:
                    number = int(c)
                    self.eliminate_row(board, number, row)
                    self.eliminate_col(board, number, col)
                    self.eliminate_box(board, number, row, col)
        
        prev_solved = -1
        new_solved = -2
                
        while prev_solved != new_solved and new_solved != 81:
            prev_solved = self.solved
            for row in range(9):
                for col in range(9):
                    t = board[row][col]
                    if type(t) == dict and t["numbers_left"] == 1:
                        for i in range(9):
                            if t["possible_numbers"][i] == 1:
                                number = i + 1
                                self.solve_cell(board, number, row, col)
            # Check box if there is a single cell with a number needed
            for row in range(3):
                for col in range(3):
                    self.check_box(board, row * 3, col * 3)

            for row in range(9):
                self.check_row(board, row)
                self.check_col(board, row)
            
            new_solved = self.solved

        if new_solved == 81:
            return True
        
        self.solve(board)
            
        print(self.solved)
        # for row in range(9):
        #     print("Row:", row)
        #     for col in range(9):
        #         print(board[row][col])
        for row in range(9):
            print("Row:", row)
            print(board[row])

        
        
        # for row in range(9):
        #     for col in range(9):
        #         if type(board[row][col]) != str:
        #             board[row][col] = "."
        # for row in range(9):
        #     print("Row:", row)
        #     print(board[row])
                    
        
s = Solution()
print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(s.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))