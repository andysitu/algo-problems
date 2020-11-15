from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]

            total_gas = g-c
            if total_gas < 0:
                continue

            if i >= len(gas)-1:
                cur_i = 0
            else:
                cur_i = i+1
            enough_gas = True
            while cur_i != i:
                print(i, cur_i)
                total_gas += gas[cur_i] - cost[cur_i]
                if total_gas < 0:
                    enough_gas = False
                    break
                if cur_i >= len(gas)-1:
                    cur_i = 0
                else:
                    cur_i += 1
            if enough_gas:
                return i
        return -1

s = Solution()
print(s.canCompleteCircuit([2,3,4], [3,4,3])== -1)
print(s.canCompleteCircuit([2],[3])==-1)
print(s.canCompleteCircuit([3],[3])==0)
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])==3)
#-2, -2, -2,  2, 2,
# linear solution might involve finding difference of gas and cost and then
# recording parts of increases and parts of decreases