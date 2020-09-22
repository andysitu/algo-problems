import sys

class Solution:
    def firstMissingPositive(self, nums) -> int:
        m = len(nums)
        min = nums[0]
        n = 0
        isaved = 0
        if min < 0:
            min = sys.maxsize
        for i in range(1, len(nums)):
            n = nums[i]
            if n > 0 and n < min:
                min = n
                if n == 1:
                    isaved = i
        if min > 1:
            return min-1
        # has 1, so record numbers into nums

        #problem: only way to guarantee that you checked all integers
        # in nums is by iterating through array each time and checking that it's ordered
        # and aligned properly
        else:
            print(isaved)
            max = m + n - 1
            i = isaved
            while i < m:
                val = nums[i]
                if val == i + min:
                    i += 1
                elif val >= min and val <= max:
                    if nums[val-min] != val:
                        temp = nums[val-min]
                        nums[val-min] = val
                        nums[i] = temp
                    else:
                        i += 1
                else:
                    i += 1
        return nums