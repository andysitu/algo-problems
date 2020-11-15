class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nlen = len(nums)
        tally = {}

        for i in range(nlen):
            u = 1 if t == 0 else t
            
            n = nums[i] // u
            if n in tally and abs(tally[n] - nums[i]) <= t:
                return True
            if n-1 in tally and abs(tally[n-1] - nums[i]) <= t:
                return True
            if n+1 in tally and abs(tally[n+1] - nums[i]) <= t:
                return True

            tally[n] = nums[i]

            if i >= k:
                del tally[nums[i-k] // u]
        return False