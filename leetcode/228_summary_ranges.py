class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nlen = len(nums)
        if nlen == 0:
            return []
        
        nlist = []
        start = nums[0]
        cur = nums[0]-1
        for i in range(len(nums)):
            if nums[i] == cur + 1:
                cur += 1
            else:
                nlist.append(str(start) + "->" + str(cur) if start != cur else str(cur))
                cur = start = nums[i]
        if cur == nums[nlen-1]:
            nlist.append(str(start) + "->" + str(cur) if start != cur else str(cur))
        return nlist