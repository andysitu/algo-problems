from typing import List

class Solution:
    def mergeSort(self, nums):
        mid = len(nums) // 2
        if mid > 0:
            left, right = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:])
            for i in range(len(nums)-1, -1, -1):
                if not right or (left and left[-1][1] > right[-1][1]):
                    l = left.pop()
                    self.answers[l[0]] += len(right)
                    nums[i] = l
                else:
                    nums[i] = right.pop()
        return nums
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        nlen = len(nums)print(cmap)print(cmap)
        self.answers = [0] * nlen
        n = list(enumerate(nums))
        self.mergeSort(n)
        return self.answers

s = Solution()
print(s.countSmaller([5,2,6,1]))