class Solution:
    def searchRange(self, nums, target: int):
        numslen = len(nums)
        # Binary search with rotation in mind
        low = 0
        high = numslen-1
        while low <= high:
            mid = int((low + high) / 2)
            value = nums[mid]
            if value == target:
                left = mid
                right = mid
                while left - 1 >= 0 and nums[left-1] == target:
                    left -= 1
                while right + 1 <= numslen - 1 and nums[right+1] == target:
                    right += 1
                return [left, right]
                    
                # binary search on right side
            elif value > target:
                high = mid -1
            else:
                low = mid + 1
        return [-1,-1]

s = Solution()
print(s.searchRange([5,7,7,8,8,10],10))