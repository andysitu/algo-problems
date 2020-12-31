class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0,1,1,0]
        if n <= 2:
            return nums[n]
        
        for i in range(3,n+1):
            nums[3] = nums[0] + nums[1] + nums[2]
            for j in range(3):
                nums[j] = nums[j+1]
        return nums[3]