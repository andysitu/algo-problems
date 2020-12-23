"""
Approach similar to three sum except you iterate
thru the nums in two for loops and then
get left and right ptrs for the final 2 numbers

Runtime: O(n^3); Space: O(n) worst case
Can decrease time by breaking out of the loops
when the smallest and largest value will be larger than target
"""

class Solution:
    def leftright(self, target, nums, l, r):
        a = []
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                a.append([nums[l],nums[r]])
                r -= 1
            elif s > target:
                r -= 1
            else:
                l += 1
        return a
                
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        nlen = len(nums)
        if nlen <= 3:
            return []
        for i in range(nlen-3):
            if len(ans) > 0 and ans[-1][0] == nums[i]:
                continue
            for j in range(i+1, nlen-2):
                if len(ans) > 0 and ans[-1][1] == nums[j] and ans[-1][0] == nums[i]:
                    continue
                results = self.leftright(target - nums[i] - nums[j], nums, j+1, nlen-1)
                for r in results:
                    if len(ans) > 0 and ans[-1][1] == nums[j] and ans[-1][0] == nums[i] and ans[-1][2] == r[0] and ans[-1][3] == r[1]:
                        continue
                    ans.append([nums[i], nums[j], r[0], r[1]])
        return ans