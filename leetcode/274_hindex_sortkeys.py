class Solution:        
    def hIndex(self, citations: List[int]) -> int:
        hdict = {}
        hmax = len(citations)
        for c in citations:
            c = min(hmax, c)
            if c not in hdict:
                hdict[c] = 1
            else:
                hdict[c] += 1
        values = list(hdict.keys())
        values.sort()
        
        hmin = 0
        
        total = 0
        for i in range(len(values)-1, -1, -1):
            v = values[i]
            if hmin > v:
                break
            total += hdict[v]
            hmax = min(v, total)
            hmin = max(hmax, hmin)
        return hmin