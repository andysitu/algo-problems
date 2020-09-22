from functools import lru_cache

class Solution:
    word1: None
    word2: None

    @lru_cache(None)
    def minWord(self, i1, i2):
        lw1 = self.lw1
        lw2 = self.lw2
        if i1 >= lw1:
            if i2 >= lw2:
                return 0
            else:
                return lw2 - i2
        elif i2 >= lw2:
            if i1 >= lw1:
                return 0
            else:
                return lw1 - i1
        
        if self.word1[i1] == self.word2[i2]:
            return self.minWord(i1+1, i2+1)
        else:
            # insert
            result = self.minWord(i1, i2+1)
            # delete
            result = min(result, self.minWord(i1+1, i2))
            # replace
            result = min(result, self.minWord(i1+1, i2+1))
        return result + 1

    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.lw1 = len(word1)
        self.lw2 = len(word2)

        self.minWord.cache_clear()

        return self.minWord(0, 0)

s = Solution()
print(s.minDistance("horse", "ros")==3)
print(s.minDistance("intention", "execution")==5)
print(s.minDistance("a", "a"))
print(s.minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine"))