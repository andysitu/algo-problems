class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        right = [1] * nlen
        s = 1
        for i in range(nlen-2, -1, -1):
            s *= nums[i+1]
            right[i] = s
        cur = 1
        for i in range(1,nlen):
            cur *= nums[i-1]
            right[i] *= cur
        return right