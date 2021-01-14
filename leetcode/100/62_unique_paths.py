class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n <= 1:
            return n
        if m == 1:
            return m

        nums = []
        for row in range(n):
            nums.append([0] * m)

        for col in range(m):
            nums[n-1][col] = 1

        for row in range(n):
            nums[row][m-1] = 1

        for col in range(m-2, -1, -1):
            for row in range(n-2, -1, -1):
                nums[row][col] = nums[row+1][col]  + nums[row][col+1]
        
        # print(nums)
        return nums[0][0]

s = Solution()
print(s.uniquePaths(3, 2)==3)
print(s.uniquePaths(7, 3)==28)
print(s.uniquePaths(1, 10)==1)
print(s.uniquePaths(10, 1)==1)
print(s.uniquePaths(14, 14)==10400600)