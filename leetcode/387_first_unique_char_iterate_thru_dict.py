class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = [1, i]
            else:
                count[s[i]][0] += 1
        for c in count:
            if count[c][0] == 1:
                return count[c][1]
        return -1