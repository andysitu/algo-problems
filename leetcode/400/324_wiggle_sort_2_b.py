from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        if nlen == 2:
            nums[0], nums[1] = min(nums[0], nums[1]), max(nums[0], nums[1]), 
            return
        small = True
        for i in range(nlen-2):
            if nums[i] == nums[i+1] == nums[i+2]:
                for j in range(nlen-1, i+2, -1):
                    if  nums[j] != nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
            n1 = max(nums[i], nums[i+1], nums[i+2])
            if n1 == nums[i]:
                n2 = max(nums[i+1], nums[i+2])
                n3 = min(nums[i+1], nums[i+2])
            elif n1 == nums[i+1]:
                n2 = max(nums[i], nums[i+2])
                n3 = min(nums[i], nums[i+2])
            else:
                n2 = max(nums[i], nums[i+1])
                n3 = min(nums[i], nums[i+1])

            if small:
                nums[i] = n3
                nums[i+1] = n1
                nums[i+2] = n2
                small = False
            else:
                nums[i] = n2
                nums[i+1] = n3
                nums[i+2] = n1
                small = True

s = Solution()
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
print(s.wiggleSort([1, 3, 2, 2, 3, 1]))
print(s.wiggleSort([1,1,1,1,1,1,3,3,3,3,3,3]))

[4,5,5,6]
[1,0]