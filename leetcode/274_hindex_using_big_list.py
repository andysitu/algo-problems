class Solution:        
    def hIndex(self, citations: List[int]) -> int:
        hmax = len(citations)
        hlist = [0] * (hmax+1)
        
        for c in citations:
            c = min(hmax, c)
            hlist[c] += 1
        
        hmin = 0
        total = 0
        for i in range(len(hlist)-1, -1, -1):
            if hmin > i:
                break
            total += hlist[i]
            hmax = min(i, total)
            hmin = max(hmax, hmin)
        return hmin