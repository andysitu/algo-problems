class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n <= 0:
            return n
        counter = 0
        end_status = False
        # Will check index ahead of counter
        while counter < n:
            if nums[counter] == val: # Duplicate found
                del nums[counter]
                n -= 1
            else:
                counter += 1
        return counter + 1