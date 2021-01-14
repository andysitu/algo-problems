class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nset = set()
        for n in nums1:
            nset.add(n)
        
        ans = set()
        for n in nums2:
            if n in nset:
                ans.add(n)
        return ans