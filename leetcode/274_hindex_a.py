class Solution:        
    def hIndex(self, citations: List[int]) -> int:
        clen = hmax = len(citations)
        if clen == 0:
            return 0
        hdict = {}
        hmin = 0
        for i in range(len(citations)):
            c = min(citations[i], hmax)
            if c < hmin:
                continue
                
            s=0            
            delList = []
            for h in hdict:
                if h <= hmin:
                    delList.append(h)
                    continue
                if c >= h:
                    hdict[h] += 1
                    if hdict[h] >= h:
                        hmin = max(hmin, h)
                        print("1", hmin, hdict)
                        delList.append(h)
                    elif h > hdict[h] and hdict[h] > hmin:
                        hmin  = max(hmin, hdict[h])
                        print("2", hmin, hdict, c)
                else:
                    s += hdict[h]
            for h in delList:
                del hdict[h]
            if c not in hdict:                    
                hdict[c] = 1 + s
        print(hdict)
                
        if hmin == 0:
            for h in hdict:
                if h > 0:
                    return 1
        return hmin