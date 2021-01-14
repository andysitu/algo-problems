class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        nummap = {}

        for i in range(1, target+1):
            nummap[i] = []
            for n in candidates:
                if n == i:
                    nummap[i].append([n])
                elif i-n <= 0 or n > i:
                    break
                else:
                    nm = nummap[i-n]
                    if len(nm) == 0:
                        continue
                    nm2 = []
                    for nmi in nm:
                        if n < nmi[len(nmi) - 1]:
                            continue
                        nm2i = list(nmi)
                        nm2i.append(n)
                        nm2.append(nm2i)
                    
                    nummap[i] = nummap[i] + nm2

        return nummap[target]

s = Solution()
l = []
for i in range(1, 31):
    l.append(i)
print(s.combinationSum(l, 500))
# print(s.combinationSum([2,3,5], 5))
# print(s.combinationSum([2,3,6,7], 7))