from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lefti = 0
        righti = len(nums)-1

        while lefti != righti:
            # print(lefti, righti)
            if lefti + 1 == righti:
                return min(nums[lefti], nums[righti])
            if nums[righti] > nums[lefti]:
                return nums[lefti]
            mid = int((lefti + righti) / 2)

            # Have to search manually
            if nums[mid] == nums[lefti] and nums[mid] == nums[righti]:
                nmin = nums[lefti]
                for i in range(lefti, righti+1):
                    nmin = min(nums[i], nmin)
                return nmin
            elif nums[mid] < nums[lefti]:
                righti = mid
            elif nums[mid] > nums[righti]:
                lefti = mid
            elif nums[mid] == nums[lefti]:
                if nums[righti] < nums[lefti]:
                    lefti = mid
                else:
                    righti = mid
            else: # nums[mid] == nums[righti]
                #if nums[lefti] < nums[rigti], Refer to top of loop
                righti = mid
        return nums[lefti]

s = Solution()
print(s.findMin([3,4,5,1,2] )==1, 1)
print(s.findMin([4,5,6,7,0,1,2] )==0, 0)
print(s.findMin([6,1,6,6,6,6,6,6,6,6,6,6,6] )==1, 1)
print(s.findMin([6,1,2,3,6, 6,6,6,6,6] )==1, 1)
print(s.findMin([6,6,6,6,6,6, 6,6,6,6,6] )==6, 6)
print(s.findMin([6,6,6,6,6,6, 6,5,5,6,6] )== 5,5)
print(s.findMin([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10] )==1, 1)
print(s.findMin([10,10, 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9] )==1, 1)
print(s.findMin([10,10,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9] )==1, 1)
print(s.findMin([10,10,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9] )==1, 1)
print(s.findMin([4,5,6,7,8,9,10],1,2,3,4 )== 1)