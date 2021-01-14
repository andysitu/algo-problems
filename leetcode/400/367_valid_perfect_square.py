class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l<= r:
            mid = (l+r)//2
            m = mid ** 2
            if m > num:
                r = mid-1
            elif m < num:
                l = mid+1
            else:
                return True
        return False