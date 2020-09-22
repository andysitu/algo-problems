class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        counter = 0
        end_status = False
        # Will check index ahead of counter
        while counter < n-1 and not end_status:
            if nums[counter] == nums[counter+1]: # Duplicate found
                del nums[counter+1]
                n -= 1
            else:
                counter += 1
        return counter + 1