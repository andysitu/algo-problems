class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cdict = {}
        maxcount = 0
        count = 0
        slen = len(s)
        prev_i = 0
        for i in range(slen):
            c = s[i]
            if not c in cdict:
                count += 1
                cdict[c] = i
            else:
                maxcount = max(maxcount, count)
                prev_i = max(cdict[c], prev_i)
                count = i-prev_i
                cdict[c] = i
        maxcount = max(count, maxcount)
        return maxcount