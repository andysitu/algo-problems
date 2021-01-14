class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        nlen = len(primes)
        vindex = [0] * nlen
        nlist = [1]
        nth = 1
        
        values = [0] * nlen
        
        while nth < n:
            nmin = float('inf')
            for i in range(nlen):
                values[i] = nlist[ vindex[i] ] * primes[i]
                nmin = min(nmin, values[i])
            for i in range(nlen):
                if values[i] == nmin:
                    vindex[i] += 1
            if nmin > nlist[nth-1]:
                nth += 1
                nlist.append(nmin)
        return nlist[nth-1]