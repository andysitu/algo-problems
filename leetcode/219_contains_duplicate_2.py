class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nlen = len(nums)
        tally = {}
        for i in range(k if nlen > k else nlen):
            if nums[i] not in tally:
                tally[nums[i]] = 0
            tally[nums[i]] += 1
            if tally[nums[i]] >=2:
                return True

        for i in range(nlen-k):
            if i > 0:
                tally[nums[i-1]] -= 1

            if nums[i+k] not in tally:
                tally[nums[i+k]] = 1
            else:
                tally[nums[i+k]] += 1

            if tally[nums[i+k]] >= 2:
                return True
            
            # if i > 0 and tally[nums[i-1]] == 0:
            #     del tally[nums[i-1]]
        return False