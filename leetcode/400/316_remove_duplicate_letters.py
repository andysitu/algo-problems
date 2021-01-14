import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        counter = collections.Counter(s)
        
        cur = 0
        for i in range(len(s)):
            if s[i] < s[cur]:
                cur = i
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                break

        return s[cur] + self.removeDuplicateLetters(s[cur+1:].replace(s[cur], ""))

s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))