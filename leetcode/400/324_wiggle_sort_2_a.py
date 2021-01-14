from typing import List

class Solution:
    def sort(self, nums, reverse, small):
        nlen = len(nums)
        if reverse:
            start, end,  inc = nlen-2, -1, -1
        else:
            start, end, inc = 0, nlen-1, 1
        for i in range(start, end, inc):
            if nums[i] == nums[i+1]:
                if not reverse:
                    for j in range(nlen-1, i+1, -1):
                        if  nums[j] != nums[i]:
                            nums[i], nums[j] = nums[j], nums[i]
                            break
                else:
                    for j in range(0, i+1):
                        if  nums[j] != nums[i]:
                            nums[i], nums[j] = nums[j], nums[i]
                            break
            n1 = max(nums[i], nums[i+1])
            n2 = min(nums[i], nums[i+1])
            
            if small:
                nums[i] = n2
                nums[i+1] = n1
                small = False
            else:
                nums[i] = n1
                nums[i+1] = n2
                small = True
        return not small

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        r = self.sort(nums, False, True)
        self.sort(nums, True, r)
        print(nums)

s = Solution()
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
print(s.wiggleSort([1, 3, 2, 2, 3, 1]))
print(s.wiggleSort([1,1,1,1,1,1,3,3,3,3,3,3]))
print(s.wiggleSort([4,5,5,6]))
print(s.wiggleSort([4,5]))
print(s.wiggleSort([5,4]))
print(s.wiggleSort([4,2,1,5,7,8,3,4,1,1,2,4,5,7,8]))
print(s.wiggleSort([2,3,3,2,2,2,1,1]))