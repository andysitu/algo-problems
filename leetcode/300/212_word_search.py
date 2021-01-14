from typing import List
from data_for_212 import a1, a2

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        foundWords = []
        initialWordDict = {}
        if board == None or len(board) == 0 or len(board[0]) == 0:
            return []

        wordTree = {}
        
        for word in words:
            t = wordTree
            for c in word:
                t = t.setdefault(c, {})
            t['*'] = word
        
        row = len(board)
        col = len(board[0])
        print(row, col)

        foundWords = []
    
        def dfs(i, j, tree):
            c = board[i][j]
            # print(c, i, j)
            t = tree[c]

            if '*' in t:
                foundWords.append(t['*'])
                del t['*']
            
            board[i][j] = '.'
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                ix, iy = i+x, j+y
                if not (0 <= ix < row and 0 <= iy < col):
                    continue
                if board[ix][iy] not in t:
                    continue
                dfs(ix, iy, t)
            board[i][j] = c

        for i in range(row):
            for j in range(col):
                if board[i][j] in wordTree:
                    dfs(i,j,wordTree)
        return foundWords

s = Solution()
print(s.findWords(a1, a2))