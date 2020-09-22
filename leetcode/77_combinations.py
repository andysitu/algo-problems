from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nlists = [[[]]]
        for i in range(k):
            nlists.append([]) 

        for i in range(k):
            prev_nlists = nlists[i]
            for nlist in prev_nlists:
                if i != 0:
                    start = nlist[i-1]
                else:
                    start = 0

                for num in range(start+1, n-(k-i)+2 ):
                    nlists[i+1].append(nlist + [num])
        return nlists[k]

s = Solution()
print(s.combine(20, 10))

# (n-(k-i))