class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1

        left = 0
        right = len(nums)-1
        while left < right -1:
            mid = int((left+right)/2)
            if (mid-1 < 0 or nums[mid-1] < nums[mid]) and (mid+1 > len(nums)-1 or nums[mid+1] < nums[mid]):
                return mid
            
            if nums[mid] < nums[mid-1]:
                right = mid
            else:
                left = mid
        return left if nums[left] >= nums[right] else right