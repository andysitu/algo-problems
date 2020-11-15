class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        if nlen == 0:
            return nums
        i, j = 0, 0
        numzeroes = 0
        
        while i < nlen:
            if nums[i] == 0:
                numzeroes += 1
                i += 1
            else:
                nums[j] = nums[i]
                j+= 1
                i+= 1
        for i in range(numzeroes):
            nums[nlen-i-1] = 0
                    