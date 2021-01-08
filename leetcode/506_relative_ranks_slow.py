class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        nums.sort(key=lambda x: x[0], reverse=True)
        ans = [1] * len(nums)
        place = 1
        for n in nums:
            if place <= 3:
                if place == 1:
                    s = "Gold Medal"
                elif place == 2:
                    s = "Silver Medal"
                else:
                    s = "Bronze Medal"
                ans[n[1]] = s
            else:
                ans[n[1]] = str(place)
            place += 1
        return ans