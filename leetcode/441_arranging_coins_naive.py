class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = 0
        level = 0
        
        while total <= n:
            level += 1
            total += level
        return level - 1