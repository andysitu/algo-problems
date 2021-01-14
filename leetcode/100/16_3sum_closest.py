import sys

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        l = len(nums)
        if l < 3:
            return ""

        values = {}
        for i in range(1, l-1):
            n1 = nums[i]
            for j in range(i+1, l):
                n = nums[j] + n1

                if n in values:
                    values[n].append(i)
                else:
                    values[n] = [i]

        incr = 0
        while True:
            for i in range(0, l-2):
                n = target - nums[i] + incr
                if n in values:
                    lv = len(values[n])
                    for j in range(lv):
                        if values[n][j] > i:
                            return nums[i] + n
                n = target - nums[i] - incr
                if n in values:
                    lv = len(values[n])
                    for j in range(lv):
                        if values[n][j] > i:
                            return nums[i] + n
            incr += 1
        
        

s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1), 2)
print(s.threeSumClosest([-3,14,-10,-1,12,13,-3,2,-6,41,3,7,-8,4,0,-13,11,-4,7,0,4,-3,12,11,5,-14,-8,8,3,-1,-8,-15,-2,-11,-9,-12,9,3,5,-11,-8,3,3,-9,-15,-12,-15,3,-9,0,-12,3,12,-14,-1,-6,-13,-2,-13,-3,12,-14,-3,-13,-9,3,-10,-15,13,2,11,13,-9,-1,11,13,-6,4,1,1,-11,5,-11,8,-2,-5,-12,-8,8,-10,4,-3,-8,-14,-1,-10,-4,-3,12,-14,14,9,6,12,-15,3,10,-13,-8,-11,3,-4,1,-1], 30))