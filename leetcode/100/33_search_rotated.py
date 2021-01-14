class Solution:
    def search(self, nums, target: int) -> int:
        numslen = len(nums)

        low = 0
        high = numslen - 1

        # Find index for lowest value
        while low < high:
            mid = int( (low + high) / 2 )
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            
        indent = low

        # Binary search with rotation in mind
        low = 0
        high = numslen-1
        while low <= high:
            mid = int((low + high) / 2)
            conv_mid = (mid + indent) % numslen
            value = nums[conv_mid]
            if value == target:
                return conv_mid
            elif value > target:
                high = mid -1
            else:
                low = mid + 1
        return -1


s = Solution()
print(s.search([4,5,6,7,-10,-9,-8,-7,-6,0,1,2],7))
print(s.search([42],7))