class BoardO:
    board = None
    pieces = 0
    def create_board(self, n):
        board = []
        for i in range(n):
            board.append([1,] * n)
        self.board = board
    
    @classmethod
    def copy_board(cls, b):
        new_board = BoardO()
        new_board.board = []
        for row in b.board:
            new_board.board.append(list(row))
        new_board.pieces = b.pieces
        return new_board

    def find_empty_spot(self, start_y=0, start_x=0):
        lenb = len(self.board)
        for i in range(start_y, lenb):
            for j in range(start_x, lenb):
                if self.board[i][j] == 1:
                    return i,j
        return -1, -1

    def place_piece(self, y, x):
        if self.board[y][x] != 1:
            return False
        else:
            self.board[y][x] = 'Q'
            self.pieces += 1

            lenb = len(self.board)
            # Straight boxes
            for i in range(lenb):
                if self.board[y][i] == 1:
                    self.board[y][i] = 0
                if self.board[i][x] == 1:
                    self.board[i][x] = 0

            # diagonal boxes
            for i in range(lenb):
                if x+i >=lenb or y+i >= lenb:
                    break
                if self.board[y+i][x+i] == 1:
                    self.board[y+i][x+i] = 0
            for i in range(lenb):
                if x - i <0 or y-i <0:
                    break
                if self.board[y-i][x-i] == 1:
                    self.board[y-i][x-i] = 0
            for i in range(lenb):
                if x+i >= lenb or y-i <0:
                    break
                if self.board[y-i][x+i] == 1:
                    self.board[y-i][x+i] = 0
            for i in range(lenb):
                if x - i <0 or y+i >= lenb:
                    break
                if self.board[y+i][x-i] == 1:
                    self.board[y+i][x-i] = 0
    def print_board(self):
        lenb = len(self.board)
        for i in range(lenb):
            print(self.board[i])
        
    def get_conv_board(self):
        lenb = len(self.board)
        b = []
        for i in range(lenb):
            row = ""
            for j in range(lenb):
                piece = self.board[i][j]
                if piece == 'Q':
                    row += "Q"
                else:
                    row += "."
            b.append(row)
        return b
        
class Solution:
    def solveNQueens(self, n: int):
        if n ==0:
            return [[]]
        boards = {}
        for i in range(1, n+1):
            boards[i] = []

        for i in range(n):
            b = BoardO()
            b.create_board(n)
            b.place_piece(0, i)
            boards[1].append(b)

        for i in range(1, n):
            boards_list = boards[i]
            for board in boards_list:
                cur_y = i
                cur_x = 0
                
                while True:
                    y, x = board.find_empty_spot(cur_y,cur_x)
                    if y == -1:
                        break
                    elif cur_y != y:
                        break
                    else:
                        b = BoardO.copy_board(board)
                        cur_x = x + 1
                        b.place_piece(y,x)
                        boards[i+1].append(b)

        blist = []
        for b in boards[n]:
            print()
            b.print_board()
            blist.append(b.get_conv_board())
        return blist

s = Solution()
print(s.solveNQueens(0))