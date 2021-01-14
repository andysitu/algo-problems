from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wmap = [None] * len(s)
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w and \
                    (i+len(w) == len(s) or wmap[i+len(w)] != None):
                    if wmap[i] == None:
                        wmap[i] = []
                    
                    # if i+len(w) == len(s):
                    wmap[i].append(w)
                    # else:
                    #     for wstr in wmap[i+len(w)]:
                    #         wmap[i].append(w + " " + wstr)
        if wmap[0] == None:
            return []
        q = []
        q.append((wmap[0], 0, ""))

        wlist = []
        
        while q:
            wordtup = q.pop()
            # print(wordtup)
            for word in wordtup[0]:
                if wordtup[1] == 0:
                    newstr = word
                else:
                    newstr = wordtup[2] + " " + word
                if len(word) + wordtup[1] == len(s):
                    wlist.append(newstr)
                else:
                    q.append((wmap[len(word) + wordtup[1]], len(word) + wordtup[1], newstr))
        return wlist


s = Solution()
# print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))

print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"]))
print(s.wordBreak("goalspecial", ["go","goal","goals","special"]))