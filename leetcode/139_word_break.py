from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = [0] * len(s)

        wordset = set(wordDict)

        for i in range(len(s)):
            pass
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