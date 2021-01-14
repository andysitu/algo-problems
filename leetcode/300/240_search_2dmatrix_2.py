class Solution:
    def bin_search(self, arr, t):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == t:
                return True
            elif arr[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        mlen = len(matrix)
        if mlen == 0 or len(matrix[0]) == 0:
            return False
        
        for i in range(mlen):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                if self.bin_search(matrix[i], target):
                    return True
            else:
                break
        return False
        