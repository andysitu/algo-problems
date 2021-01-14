from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        lim1, lim2 = len(nums1), len(nums2)
        if lim1 == 0 or lim2 == 0:
            return []
        nums_heap = [[ nums1[i] + nums2[0], [nums1[i], nums2[0]], i, 0] for i in range(lim1 if lim1 < k else k)]
        heapq.heapify(nums_heap)
        ans = []
        for _ in range(k):
            if not nums_heap:
                return ans
            a = heapq.heappop(nums_heap)
            ans.append(a[1])
            if a[3] < lim2-1:
                heapq.heappush(nums_heap, [ nums1[a[2]] + nums2[a[3]+1], [nums1[a[2]], nums2[a[3]+1]], a[2], a[3]+1 ])
        return ans
        

s = Solution()
print(s.kSmallestPairs([1, 1, 2, 2, 2, 4, 6, 6, 8, 8, 9, 11, 13, 14, 19, 22, 22, 27, 27, 33, 35, 37, 38, 42, 43, 45, 46, 47, 48, 49, 51, 52, 54, 54, 55, 62, 63, 64, 66, 68, 72, 73, 74, 75, 76, 77, 78, 78, 78, 80, 81, 83, 84, 86, 91, 94, 96, 97, 105, 106, 108, 109, 114, 114, 121, 124, 124, 128, 136, 136, 137, 140, 143, 144, 149, 150, 151, 159, 163, 165, 165, 166, 167, 175, 178, 182, 183, 187, 188, 188, 189, 189, 189, 190, 191, 194, 195, 198, 198, 198],
[1, 1, 2, 2, 2, 4, 6, 6, 8, 8, 9, 11, 13, 14, 19, 22, 22, 27, 27, 33, 35, 37, 38, 42, 43, 45, 46, 47, 48, 49, 51, 52, 54, 54, 55, 62, 63, 64, 66, 68, 72, 73, 74, 75, 76, 77, 78, 78, 78, 80, 81, 83, 84, 86, 91, 94, 96, 97, 105, 106, 108, 109, 114, 114, 121, 124, 124, 128, 136, 136, 137, 140, 143, 144, 149, 150, 151, 159, 163, 165, 165, 166, 167, 175, 178, 182, 183, 187, 188, 188, 189, 189, 189, 190, 191, 194, 195, 198, 198, 198],
140))