import queue

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        clist = [0] * 26
        maxc = 0
        maxlen = 0
        for i in range(len(s)):
            clist[ord(s[i]) - ord('A')] += 1
            maxc = max(clist[ord(s[i]) - ord('A')], maxc)
            
            while (i - start + 1 - maxc) > k:
                clist[ord(s[start]) - ord('A')] -= 1
                start += 1
            maxlen = max(maxlen, i-start+1)
        return maxlen