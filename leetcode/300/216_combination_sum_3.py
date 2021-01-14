from typing import List

class Solution:
    def combine_sum(self,start, k, target, solution, path):
        for i in range(start, 10):
            if i > target:
                return
            elif i == target and len(path) == k-1:
                solution.append(path+[i,])
                return
            else:
                if len(path) < k:
                    self.combine_sum(i+1, k, target-i, solution, path + [i,])

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        solution = []
        self.combine_sum(1, k, n, solution, [])
        return solution

s = Solution()
print(s.combinationSum3(9,3))