class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        nlist = [1] * (n+1)
        for i in range(2, n):
            if nlist[i] == 1:
                primes += 1
                m = i
                while m <= n:
                    nlist[m] = 0
                    m += i
        return primes

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        nlist = [1] * (n+1)
        for i in range(2, n):
            if nlist[i] == 1:
                primes += 1
                nlist[i*i: n: i] = [0] * len(nlist[i*i:n : i])
        return primes