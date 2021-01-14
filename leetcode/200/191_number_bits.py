class Solution:
    def hammingWeight(self, n: int) -> int:
        totalbits = 0
        newn = n

        for i in range(32):
            totalbits += newn&1
            newn >>=1
        return totalbits