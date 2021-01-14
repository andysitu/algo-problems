class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        delta = 0.0001
        left = 1
        right = x

        mid = (right + left) / 2
        m = mid * mid
        diff = m - x

        while abs(diff) > delta or diff < 0:
            mid = (right + left) / 2
            m = mid * mid
            if m == x:
                return int(mid)
            elif m > x:
                right = mid
            else:
                left = mid
            diff = m - x

        return int(mid)

s = Solution()
print(s.mySqrt(2147395599))