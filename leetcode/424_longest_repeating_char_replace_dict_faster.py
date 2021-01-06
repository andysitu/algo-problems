import queue

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        cmap = {}
        maxc = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in cmap:
                cmap[s[i]] += 1
            else:
                cmap[s[i]] = 1
            maxc = max(cmap[s[i]], maxc)
            
            while (i - start + 1 - maxc) > k:
                cmap[s[start]] -= 1
                start += 1
            maxlen = max(maxlen, i-start+1)
        return maxlen