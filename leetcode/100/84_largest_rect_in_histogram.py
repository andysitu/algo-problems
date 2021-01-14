from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hlen = len(heights)
        if hlen == 0:
            return 0

        leftindex = [-1] * hlen
        rightindex = [-1] * hlen

        leftindex[0] = -1
        rightindex[hlen-1] = hlen

        for i in range(1, hlen):
            if heights[i] <= heights[i-1]:
                a = leftindex[i-1]
                while a >= 0 and heights[a] >= heights[i]:
                    a -= 1
                leftindex[i] = a
            else:
                leftindex[i] = i-1
        
        for i in range(hlen -2, -1, -1):
            if heights[i] <= heights[i+1]:
                a = rightindex[i+1]
                while a <= hlen - 1 and heights[a] >= heights[i]:
                    a += 1
                rightindex[i] = a
            else:
                rightindex[i] = i+1

        maxarea = 0
        for i in range(hlen):
            # print(i, rightindex[i], leftindex[i])
            maxarea = max(maxarea, heights[i] * (rightindex[i] - leftindex[i] - 1))

        print(heights)
        print(leftindex)
        print(rightindex)
        
        return maxarea

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))

# print(s.largestRectangleArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
 
# a = []

# for i in range(20000):
#     a.append(i+1)

# print(s.largestRectangleArea(a))

# a = []

# for i in range(20000):
#     a.append(20000-i)

# print(s.largestRectangleArea(a))
