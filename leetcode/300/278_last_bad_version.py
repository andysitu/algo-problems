# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        lastbad = -1
        while start < end:
            mid = start + (end-start) // 2
            if isBadVersion(mid):
                lastbad = mid
                end = mid-1
            else:
                start = mid+1
        return start if isBadVersion(start) else lastbad