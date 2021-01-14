class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        twoindex = 0
        threeindex = 0
        fiveindex = 0
        nlist=[1]
        nth = 1
        
        while nth < n:
            two = nlist[twoindex] * 2
            three = nlist[threeindex] * 3
            five = nlist[fiveindex] * 5
            if two <= three and two <= five:
                nmin = two
                if two == three:
                    threeindex += 1
                if two == five:
                    fiveindex += 1
                twoindex += 1
            elif three <= two and three <= five:
                nmin = three
                if two == three:
                    twoindex += 1
                if three == five:
                    fiveindex += 1
                threeindex += 1
            else:
                nmin = five
                if two == five:
                    twoindex += 1
                if three == five:
                    threeindex += 1
                fiveindex += 1
            if nmin > nlist[nth-1]:
                nth += 1
                nlist.append(nmin)
        return nlist[nth-1]