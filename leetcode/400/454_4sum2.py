class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d1 = {}
        for n1 in A:
            for n2 in B:
                if n1 + n2 not in d1:
                    d1[n1+n2] = 1
                else:
                    d1[n1+n2] += 1
        s = 0
        for n1 in C:
            for n2 in D:
                if -n1 - n2 in d1:
                    s += d1[-n1-n2]
        return s