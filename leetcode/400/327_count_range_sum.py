from typing import List;

class Solution:
    def mergesort(self, nums, lower, upper):
        nlen = len(nums)
        mid = nlen // 2
        if mid > 0:
            left, right = self.mergesort(nums[:mid],lower,upper), self.mergesort(nums[mid:],lower,upper)
            
            rlen = len(right)
            i=j=0
            for l in range(len(left)):
                while i < rlen and right[i] - left[l] < lower:
                    i += 1
                while j < rlen and right[j] - left[l] <= upper:
                    j += 1
                self.answers += j - i

            for i in range(nlen-1, -1, -1):
                if not right or (left and left[-1] > right[-1]):
                    l = left.pop()
                    nums[i] = l
                else:
                    nums[i] = right.pop()
        return nums

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.answers = 0
        leftsum = [0]
        for n in nums:
            leftsum.append(n + leftsum[-1])
        self.mergesort(leftsum, lower, upper)
            
        return self.answers

s = Solution()
print(s.countRangeSum([-2,5,-1], -2, 2))
print(s.countRangeSum([2,-4,1,3,-3,6,5], -3, 3))