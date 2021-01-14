from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def bs(nlist, x):
            l, r = 0, len(nlist)-1
            while l <= r:
                mid = (l + r) // 2
                if nlist[mid]["y"] < x:
                    l = mid+1
                elif nlist[mid]["y"] > x:
                    r = mid-1
                else:
                    return mid
            return r
        elen = len(envelopes)
        if elen == 0:
            return 0
        # sort by x, and then sort by y in 2d array
        envelopes.sort()
        dp = []
        cur_x = envelopes[0][0]
        e = []
        for i in range(elen):
            if envelopes[i][0] != cur_x:
                cur_x = envelopes[i][0]
                dp.append(e)
                e = [{ "y":envelopes[i][1], "value": 1},]
            else:
                e.append({ "y":envelopes[i][1], "value": 1},)
        dp.append(e)
        
        maxn = 1
        prev=(-1,-1)
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                y =dp[i][j]["y"]
                for k in range(i-1,-1,-1):
                    if dp[k][0]["y"] >= y:
                        continue
                    index = bs(dp[k], y)-1
                    if dp[i][j]["y"] == dp[k][index]["y"]:
                        dp[i][j]["value"] = dp[k][index]["value"]
                    else:
                        dp[i][j]["value"] = dp[k][index]["value"] + 1
                    maxn = max(maxn, dp[i][j]["value"])
                    break
        print(dp)
        return maxn


s = Solution()
# print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

s2 = [[-5, 17], [7, 11], [-6, 15], [-10, 6], [-1, 14], [14, 8], [3, -7], [19, 16], [5, -10], [6, 5], [6, 2], [3, -10], [0, -8], [12, 17], [0, 6], [7, -7], [2, -10], [-2, -10], [6, 14], [-2, -2], [1, 15], [11, 3], [3, 20], [20, 8], [12, 9], [-3, -10], [-10, 20], [10, 13], [15, 12], [8, -2], [-7, 12], [20, 0], [-5, -1], [2, -1], [1, -2], [-2, -9], [2, 9], [2, -6], [11, 2], [19, 1], [-6, 15], [4, 8], [16, 19], [17, 10], [15, -5], [3, 20], [14, 1], [4, -5], [2, 18], [10, 10], [5, 17], [7, 16], [16, 9], [14, -3], [6, 17], [-10, -9], [-2, 2], [8, -10], [1, 1], [-1, 15], [13, 0], [12, 2], [0, 19], [14, 10], [2, 6], [2, -7], [8, -4], [20, 14], [14, 19], [0, 9], [5, 3], [0, -2], [8, -5], [12, 3], [14, 5], [-9, 11], [4, 5], [-3, 16], [-4, -10], [1, 9], [7, -8], [-8, 2], [14, 13], [15, 12], [19, 5], [14, 12], [-2, 6], [19, 0], [-6, 6], [8, -7], [18, 0], [18, -1], [1, -10], [18, 13], [7, 16], [3, 16], [9, 4], [14, 12], [5, 14], [15, -9]]
print(s.maxEnvelopes(s2))