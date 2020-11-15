class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums == None:
            return nums
        nlimit = (len(nums) // 3) + 1
        
        n1, n2, n1i, n2i = None, None, 0, 0
        
        for n in nums:
            if n1i == 0 and n != n2:
                n1i = 1
                n1 = n
            elif n2i == 0 and n!= n1:
                n2i = 1
                n2 = n
            elif n1 == n:
                n1i += 1
            elif n2 == n:
                n2i += 1
            else:
                n1i, n2i = n1i - 1, n2i - 1
        return [ n for n in (n1, n2) if nums.count(n) > len(nums) // 3]