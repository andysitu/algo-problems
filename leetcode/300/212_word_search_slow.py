from typing import List
from data_for_212 import a1, a2

# Can use a dictionary to search all the words at once through the board
# Dictionary will contain a structure similar to the prefix/ trie word problems

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        foundWords = []
        initialWordDict = {}
        if board == None or len(board) == 0 or len(board[0]) == 0:
            return []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in initialWordDict:
                    initialWordDict[board[i][j]] = []
                initialWordDict[board[i][j]].append((i,j))
        
        for w in words:
            if w[len(w)-1] in initialWordDict and w[0] in initialWordDict:
                if len(initialWordDict[w[len(w)-1]]) < len(initialWordDict[w[0]]):
                    for index_tup in initialWordDict[w[len(w)-1]]:
                        if self.travel(board, w, len(w)-1, -1, index_tup[0], index_tup[1], set(), set()):
                            foundWords.append(w)
                            break
                else:
                    for index_tup in initialWordDict[w[0]]:
                        if self.travel(board, w, 0, 1, index_tup[0], index_tup[1], set(), set()):
                            foundWords.append(w)
                            break
        return foundWords
    
    def travel(self, board, word, word_index, index_inc, i, j, travelled_set, travelled):
        if word_index < 0 or word_index >= len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if (i,j) in travelled_set or board[i][j] != word[word_index]:
            return False
        
        if (i,j, word_index) in travelled:
            return False

        s = set(travelled_set)
        s.add((i,j))

        if self.travel(board, word, word_index + index_inc, index_inc, i+1, j, set(s), travelled):
            return True
        if self.travel(board, word, word_index + index_inc, index_inc, i-1, j, set(s), travelled):
            return True
        if self.travel(board, word, word_index + index_inc, index_inc, i, j+1, set(s), travelled):
            return True
        if self.travel(board, word, word_index + index_inc, index_inc, i, j-1, set(s), travelled):
            return True
        travelled.add((i,j,word_index))
        return False

s = Solution()
print(s.findWords(a1, a2))