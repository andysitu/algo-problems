from typing import List

class Solution:
    def find_fit(self, s, start, wordDict):
        if start >= len(s):
            return True
        for i in range(start+1, len(s)+1):
            if self.bad_result[start][i] == 1:
                return False
            if s[start:i] in wordDict:
                if self.find_fit(s, i, wordDict):
                    return True
                else:
                    self.bad_result[start][i] = 1
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.bad_result = []
        for i in range(len(s)):
            self.bad_result.append([0] * (len(s)+1) )
        self.max_word = 1
        for w in wordDict:
            self.max_word = max(self.max_word, len(w))
        return self.find_fit(s, 0, wordDict)

s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]) == True)
print(s.wordBreak("applepenapple", ["apple", "pen"]) == True)
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)

p = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
b = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(s.wordBreak(p, b) == False)
print(s.wordBreak("goalspecial", ["go","goal","goals","special"]) == True)

print(s.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"]))