from typing import List

class Solution:
    def sort(self, nums, start, end):
        if end < start:
            return
        print(start, nums[start])
        if end == start:
            return
        i,j,k = start, start+1, end
        while j <= k:
            # print(nums)
            if nums[i][0] >= nums[j][0]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                nums[k], nums[j] =  nums[j], nums[k]
                k -= 1
        print(i)
        
        self.sort(nums, start, i-1)
        self.sort(nums, i+1, end)
            
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        self.answers = [0] * nlen
        n = []
        for i in range(nlen):
            n.append((nums[i], i))
        self.sort(n, 0, nlen-1)
        return self.answers

s = Solution()
print(s.countSmaller([5,2,6,1]))