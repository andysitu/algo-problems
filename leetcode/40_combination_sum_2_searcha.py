class Solution:
    def combine_sum(self, nums, start, path, sums, target):
        if target == 0:
            sums.append(path)
            return
        for i in range(start, len(nums)):
            n = nums[i]
            if n > target:
                break

            if i > start and nums[i-1] == n:
                continue

            self.combine_sum(nums, i+1, path + [n,], sums, target-n)
        

    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        sums = []
        self.combine_sum(candidates, 0, [], sums, target)
        return sums
            
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5,8,9,10,32,12], 21))
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# print(s.combinationSum2([], 15))