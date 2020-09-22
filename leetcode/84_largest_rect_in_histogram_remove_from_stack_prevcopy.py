from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        hlen = len(heights)

        height_stack = [0] * hlen
        index_stack = [0] * hlen
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

            current_stack_index = stack_index

            index = current_stack_index

            while index > -1:
                if height_stack[index] > h:
                    height_stack[index] = h
                
                if height_stack[index] * (i - index_stack[index]  + 1) > area:
                    area = height_stack[index] * (i - index_stack[index]  + 1)
                    area_index = index_stack[index]
                    # print("new", height_stack[index], index_stack[index], area)
                    stack_index = index
                index -= 1

            stack_index += 1
            height_stack[stack_index] = h
            index_stack[stack_index] = i
            maxarea = max(maxarea, area)
            # print(i, h, area)
            # print(height_stack)
            # print(index_stack)

        return maxarea

s = Solution()
# print(s.largestRectangleArea([2,1,5,6,2,3]))

# print(s.largestRectangleArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

a = []

for i in range(20000):
    a.append(i+1)

print(s.largestRectangleArea(a))

# a = []

# for i in range(20000):
#     a.append(20000-i)

# print(s.largestRectangleArea(a))