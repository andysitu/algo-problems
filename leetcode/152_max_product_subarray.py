class Solution:
    def findMax(self, nums, start, last):
        if start == last:
            return nums[start]

        negindices = []
        for i in range(start, last+1):
            if nums[i] == 0:
                if i == 0:
                    return max(0, self.findMax(nums, i+1, last))
                elif i == last:
                    return max(0, self.findMax(nums, start, i-1))
                else:
                    n1 = self.findMax(nums, start, i-1)
                    n2 = self.findMax(nums, i+1, last)
                    return max(n1, n2, 0)
            if nums[i] < 0: 
               negindices.append(i)

        num_neg = len(negindices)

        if num_neg == 1:
            if negindices[0] == start:
                return max(self.findMax(nums, negindices[0]+1, last), nums[negindices[0]])
            elif negindices[0] == last:
                return max(self.findMax(nums, start, negindices[0]-1), nums[negindices[0]])
            else:
                n1 = self.findMax(nums, negindices[0]+1, last)
                n2 = self.findMax(nums, start, negindices[0]-1)
                return max(n1, n2, nums[ negindices[0] ])
            return max(n1, n2, -1)
        elif num_neg % 2 == 0:
            prod = 1
            for i in range(start, last+1):
                prod *= nums[i]
            return prod
        else:
            first_neg_index = negindices[0]
            last_neg_index = negindices[-1]
            return max(
                self.findMax(nums, start, first_neg_index),
                self.findMax(nums, first_neg_index+1, last), 
                self.findMax(nums, last_neg_index, last),
                self.findMax(nums, start , last_neg_index-1),
            )

    def maxProduct(self, nums: List[int]) -> int:
        return self.findMax(nums, 0, len(nums)-1)


"""
[2,3,-2,0, 4,-2, -1, 4, 10, 0, 3, 2, 5, 10, -1, -1, 4]
"""