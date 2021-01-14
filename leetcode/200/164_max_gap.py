from typing import List
# radix sorting
# can use 1 bucket and another list of counts for each 
# "individual" bucket and iterate backwards for much faster and less space

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        buckets = [ [] for i in range(10) ]
        
        for n in nums:
            buckets[n % 10].append(n)
        # print(buckets)

        cstatus = True
        digit = 0
        while cstatus:
            new_buckets = [ [] for i in range(10) ]
            cstatus = False
            digit += 1
            for d in range(len(buckets)):
                for n in buckets[d]:
                    r = int(n / (10 ** digit)) % 10
                    if not cstatus and n >= 10 ** digit:
                        cstatus = True
                    # print(r, n, digit)
                    new_buckets[r].append(n)
            buckets = new_buckets
        maxdiff = 0
        for i in range(len(buckets[0])-1):
            maxdiff = max(maxdiff, buckets[0][i+1] - buckets[0][i])
        return maxdiff
        


s = Solution()
print(s.maximumGap([1, 10000000]))