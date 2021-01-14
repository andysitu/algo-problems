class Solution:
    def jump(self, nums) -> int:
        numslen = len(nums)
        record = [-1] * numslen
        record[numslen-1] = 0

        for i in range(numslen-2, -1, -1):
            n  = nums[i]

            if i + n >= numslen-1:
                record[i] = 1
                continue
            
            minstep = numslen
            for step in range(1, n+1):
                new_step = i+step
                if record[new_step] < minstep:
                    minstep = record[new_step]
            record[i] = minstep + 1
        return record[0]