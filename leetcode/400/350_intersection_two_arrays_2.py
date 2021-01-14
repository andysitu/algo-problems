class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nset = {}
        for n in nums1:
            if n not in nset:
                nset[n] = 1
            else:
                nset[n] += 1
        
        ans = []
        for n in nums2:
            if n in nset:
                nset[n] -= 1
                if nset[n] == 0:
                    del nset[n]
                ans.append(n)
        return ans