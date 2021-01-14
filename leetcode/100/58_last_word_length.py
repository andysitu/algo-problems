class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nlen = len(s)

        l = 0
        for i in range(nlen-1, -1, -1):
            if s[i] == ' ' and l > 0:
                break
            elif s[i] == ' ':
                continue
            else:
                l += 1
        return l