from typing import List

class Solution:
    def print_minh(self, minheights):
        mhlen = len(minheights)
        for i in range(mhlen):
            print(minheights[i])

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        minheights = []

        hlen = len(heights)

        for i in range(hlen):
            minheights.append([])

        for l in range(hlen):
            for i in range(l):
                minheights[l].append(0)

            minheights[l].append(heights[l])
            maxarea = max(maxarea, heights[l])
            for r in range(l+1, hlen):
                minheights[l].append( min( minheights[l][r-1], heights[r]) )
                maxarea = max(maxarea, (r-l+1) * minheights[l][r])

        self.print_minh(minheights)                  
        return maxarea

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([19, 56, 22, 24, 37, 52, 45, 74, 28, 50, 72, 31, 21, 9]))