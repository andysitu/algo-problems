class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        nummap = [set()] + [set() for i in range(target)]

        for n in candidates:
            if n > target:
                break

            for j in range(target - n, 0, -1):
                for numset in nummap[j]:
                    nummap[j+n].add((n,) + numset)
            nummap[n].add((n,))

        return nummap[target]
        
            
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5,8,9,10,32,12], 15))
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# print(s.combinationSum2([], 15))