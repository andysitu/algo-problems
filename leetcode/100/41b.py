class Solution:
    def firstMissingPositive(self, nums) -> int:
        smallest = nums[0]
        n = 0
        if smallest < 0:
            smallest = 0
        for i in range(1, len(nums)):
            n = nums[i]
            if n > 0 and n < smallest:
                smallest = n
        if smallest > 1:
            return smallest-1
        else:
            nums.sort()
            smallest = 0
            for i in range(0, len(nums)):
                if smallest >= nums[i]:
                    continue
                if nums[i] > 0:
                    smallest += 1
                    if nums[i] != smallest:
                        return smallest
            return smallest + 1

s = Solution()
print(s.firstMissingPositive([7,8,9,11,12]))
print(s.firstMissingPositive([10,9,8,7,6]))
print(s.firstMissingPositive([5,4,3,2,1]))
print(s.firstMissingPositive([1,2,0,3,3,3,4,5,6]))