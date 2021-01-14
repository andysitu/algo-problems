class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numslen = len(nums)
        # Go backwards & find num after that is larger than it
        max_i_val = -1
        ivalue = -1
        for i in range(numslen-1, -1, -1):
            if nums[i] > max_i_val:
                max_i_val = nums[i]
                ivalue = i
            elif nums[i] < max_i_val:
                print(i, nums[i], ivalue)

                temp = nums[i]
                nums[i] = nums[ivalue]
                nums[ivalue] = temp
                # Switch from values i + 1 to end of nums
                # by flipping them since it's guaranteed to the largest value for  the subset
                prev_j = -1
                for j in range(i+1, numslen):
                    index = numslen - j + i
                    if index < j: # Stop if switching indices cross
                        break
                    temp = nums[j]
                    nums[j] = nums[index]
                    nums[index] = temp
                    if index == j: # Stop after transfer
                        break
        if ivalue == -1:
            nums.sort()
        return nums

s = Solution()
# print(s.nextPermutation([5,4,2,4,1,2,3,4,5,6,7]))
# print(s.nextPermutation([6,7,5,3,2,1]))
print(s.nextPermutation([1,3,2]))