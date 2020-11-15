class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        s = 0
        nset = set()
        for n in nums:
            s += n
            if n not in nset:
                nset.add(n)
        
        for n in nset:
            s -= (n*3)
        return -(s//2)