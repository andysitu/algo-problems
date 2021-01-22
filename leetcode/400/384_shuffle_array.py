import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.copy = [x for x in nums]
        self.l = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        for i in range(self.l):
            self.copy[i] = self.original[i]
        return self.original
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.l):
            p = random.randint(0, self.l-1)
            self.copy[i], self.copy[p] = self.copy[p], self.copy[i]
        return self.copy
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()