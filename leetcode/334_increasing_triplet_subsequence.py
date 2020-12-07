class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        a = [nums[0], float('inf'), float('inf')]
        
        for i in range(1, len(nums)):
            if nums[i] > a[0] and nums[i] > a[1]:
                return True
            if nums[i] > a[0]:
                a[1] = nums[i]
            else:
                a[0] = nums[i]
        return False