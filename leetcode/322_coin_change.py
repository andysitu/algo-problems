from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        amounts = {amount: 0}

        asets = set()
        asets.add(amount)

        new_coin = []
        for c in coins:
            if c == amount:
                return 1
            if c < amount:
                new_coin.append(c)
        new_coin.sort(reverse=True)

        while amounts:
            new_amounts = {}
            for a in amounts:
                for c in new_coin:
                    left = a-c
                    if left < 0:
                        continue
                    if left == 0:
                        return amounts[a] + 1
                    
                    if left in asets:
                        continue
                    else:
                        new_amounts[left] = amounts[a]+1
                        asets.add(left)
            amounts = new_amounts
        return -1


s = Solution()
# print(s.coinChange([1,2,5], 11))
print(s.coinChange([1], 1))