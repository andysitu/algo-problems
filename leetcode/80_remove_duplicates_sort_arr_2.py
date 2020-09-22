from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nlen = len(nums)

        read_i = 0
        write_i = 0
        prev_n = -1
        first_n_index = 0

        while read_i < nlen:
            n = nums[read_i]
            if prev_n != n:
                first_n_index = read_i

            if read_i - first_n_index < 2:
                nums[write_i] = n
                write_i += 1
            read_i += 1
            prev_n = n
        return write_i

s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3,3,3,3,4,5,6,6,6,6,6,6,6,6,6,7]))