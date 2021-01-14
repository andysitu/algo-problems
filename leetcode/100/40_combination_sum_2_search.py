class Solution:
    def combine_sum(self, nums, start, path, result, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            self.combine_sum(nums, i + 1, path + [nums[i]], result, target-nums[i])

    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        result = []
        self.combine_sum(candidates, 0, [], result, target)

        return result
        
            
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5,8,9,10,32,12], 20))
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# print(s.combinationSum2([], 15))