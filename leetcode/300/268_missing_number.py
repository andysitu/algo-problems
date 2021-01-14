class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nlen = len(nums)
        for i in range(nlen):
            if nums[i] == i:
                continue
            elif nums[i] >= nlen:
                continue
            else:
                j = nums[i]
                while j < nlen and nums[j] != j:
                    t= nums[j]
                    nums[j] = j
                    j = t
        for i in range(nlen):
            if nums[i] != i:
                return i
        return nlen