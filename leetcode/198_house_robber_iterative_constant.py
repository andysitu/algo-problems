class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p1 = 0
        p2 = 0
        for n  in nums:
            m = max(p1, p2+ n)
            p2 = p1
            p1 = m
        return m