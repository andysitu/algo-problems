from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        slen = len(s)
        if slen % 2 == 0:
            end = int(slen / 2)
        else:
            end = int(slen / 2) + 1
        
        for i in range(end):
            # print(s[i], s[-i], i)
            if s[i] != s[slen-i-1]:
                return False
        return True

    def build_str(self, s, start, end, palin_map):
        if start > end:
            return [[],]
        words = []
        for i in range(start, end+1):
            if s[start] == s[i]:
                w = s[start:i+1]
                if w in palin_map:
                    if palin_map[w]:
                        pass
                else:
                    if self.isPalindrome(w):
                        wordlists = self.build_str(s, i+1, end, palin_map)
                        for wlist in wordlists:
                            words.append([w,] + wlist)
                # print(s[start:i+1])
        return words

    def partition(self, s: str) -> List[List[str]]:
        return self.build_str(s, 0, len(s) - 1, {})

s = Solution()

print(s.partition("aab"))
print(s.partition("aabab"))
print(s.partition(""))