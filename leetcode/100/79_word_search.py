from typing import List

class Solution:
    wordlen = -1
    board = None
    nrows = -1
    ncols = -1
    
    def explore(self, i, j, index):
        # print(i,j, index)
        if i < 0 or i >= self.nrows or j < 0 or j >= self.ncols:
            return False
        if index >= self.wordlen or self.board[i][j] != self.word[index]:
            return False
        
        tempc = self.board[i][j]
        self.board[i][j] = "."
        if index == self.wordlen - 1:
            # print("va", i, j, index, self.word[index], self.wordlen)
            return True

        # print("v", i, j, index, self.word[index], self.wordlen, self.visited)

        result = self.explore(i-1, j, index+1) or self.explore(i, j-1, index+1) or self.explore(i, j+1, index+1) or self.explore(i+1, j, index+1)
        if result:
            return True

        # print("false", i, j)
        self.board[i][j] = tempc
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.nrows = len(board)
        self.ncols = len(board[0])
        
        self.wordlen = len(word)
        self.board = board
        self.word = word

        for i in range(self.nrows):
            for j in range(self.ncols):
                c = board[i][j]
                if c == word[0]:
                    result = self.explore(i, j, 0)
                    if result:
                        return True
        return False


s = Solution()
print(s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED")==True)
print(s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABC")==True)

print(s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCEE")==False)

print(s.exist(
[["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]],
"ABCESEEEFS"
)==True)

print(s.exist(
[["a","b"],["c","d"]],
"abcd"
)==False)

print(s.exist(
[["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]],
"ABCEEDE"
)==False)