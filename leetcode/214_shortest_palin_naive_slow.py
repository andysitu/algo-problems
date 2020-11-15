class Solution:
    def shortestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen == 1:
            return s
        dp = [[0] * slen for _ in range(slen)]

        max_size = 1
        max_indices = None
        for i in range(slen - 2, -1, -1):
            for j in range(i+1, slen):
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if i == 0 and j-i+1 > max_size:
                        max_size = j-i+1
                        max_indices = (i,j)
        if max_size > 1:
            left, right = max_indices
            strlist = []
            for i in range(slen-1, right, -1):
                strlist.append(s[i])
            return "".join(strlist) + s
        else:
            strlist = []
            for i in range(slen-1, 0, -1):
                strlist.append(s[i])
            return "".join(strlist) + s