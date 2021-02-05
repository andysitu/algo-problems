class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        mem = ['a', 0]
        total = 0
        for i in range(1,len(A)):
            if A[i-1] - A[i] == mem[0]:
                mem[1] += 1
                total += mem[1]
            else:
                mem = [A[i-1] - A[i], 0]
        return total