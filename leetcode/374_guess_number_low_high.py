# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        mid, result = 0,0
        while l <= r:
            mid = (l+r)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                l = mid + 1
            else:
                r = mid - 1
        return l
            