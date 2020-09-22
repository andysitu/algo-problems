from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        hlen = len(heights)

        height_stack = []
        index_stack = []
        stack_index = -1
                
        if hlen == 0:
            return 0

        for i in range(hlen):
            h = heights[i]

            area = h
            area_index = i
            density = h

            # print("\ni", i)
            # print(height_stack)
            # print(index_stack)

            index = len(height_stack) - 1

            while index > -1:
                if height_stack[index] > h:
                    height_stack[index] = h
                
                if height_stack[index] * (i - index_stack[index]  + 1) > area:
                    area = height_stack[index] * (i - index_stack[index]  + 1)
                    area_index = index_stack[index]
                    # print("new", height_stack[index], index_stack[index], area)
                elif index_stack[index] < area_index:
                    del height_stack[:index]
                    del index_stack[:index]
                    break
                index -= 1

            height_stack.append(h)
            index_stack.append(i)

            maxarea = max(maxarea, area)

            # print("i", i, "h", h, "maxarea", maxarea) 
            
            # print("area", area, "areah", height_stack[index], "areai", area_index, "heightstacklen", len(height_stack))
            # print(height_stack)
            # print(index_stack)
        print(len(height_stack))
        return maxarea

s = Solution()
# print(s.largestRectangleArea([2,1,5,6,2,3]))

print(s.largestRectangleArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

a = []

for i in range(20000):
    a.append(i+1)

print(s.largestRectangleArea(a))

# a = []

# for i in range(20000):
#     a.append(20000-i)

# print(s.largestRectangleArea(a))