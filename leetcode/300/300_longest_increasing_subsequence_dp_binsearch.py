class Solution:
    def bs(self, arr, target):
        start, end = 0, len(arr)-1
        while start <= end:
            mid = start + (end-start) // 2
            
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                return mid
        return start
            
    def lengthOfLIS(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen == 0:
            return 0
        
        dp = []
                
        for i in range(nlen):
            index = self.bs(dp, nums[i])
            if index == len(dp):
                dp.append(nums[i])
            else:
                dp[index] = nums[i]
        return len(dp)