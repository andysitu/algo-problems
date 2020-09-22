class Solution:
    def firstMissingPositive(self, nums) -> int:
        m = len(nums)
        for i in range(m):
            # print('i', i)
            val = nums[i]
            if (i+1) != val and val >= 1 and val <= m:
                while val >= 1 and val <= m and nums[val - 1] != val:
                    temp = nums[val - 1]
                    # print('val', val)
                    # print("temp", temp)
                    nums[val - 1] = val
                    val = temp
        for i in range(m):
            if nums[i] != i +1:
                return i + 1
        return m + 1

s = Solution()
print(s.firstMissingPositive([3,4,-1,1]))
print(s.firstMissingPositive([7,8,9,11,12]))
print(s.firstMissingPositive([10,9,8,7,6]))
print(s.firstMissingPositive([5,4,3,2,1]))
print(s.firstMissingPositive([1,2,0,3,3,3,4,5,6]))
print(s.firstMissingPositive([-1,7,8,10,101,-4,0,1,1,2,0,3,3,3,4,5,6]))