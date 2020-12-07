class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join([str(x) for x in b])), 1337)