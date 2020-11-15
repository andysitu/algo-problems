from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)

        ratingtup = []


        ratingtup= sorted(ratingtup, key=lambda ratingtup: ratingtup[0])

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i +1]:
                candy[i] = candy[i +1] + 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i -1] and candy[i] <= candy[i - 1]:
                candy[i] = candy[i - 1] + 1

        # print(ratingtup)
        # print(candy)

        sumcandy = 0
        for x in candy:
            sumcandy += x
        return sumcandy

s = Solution()
print(s.candy([1,0,2]))
print(s.candy([2,4,5,2,1,1,2,3,2,2,1,2,3,4]))
# print(s.candy([]))
print(s.candy([1,2,2]))
s1 = [1,0,3,4,2,1,3,2,4,2,3,1,2,3,4,5,6,24,2,3,4,1,2,3,2,4,1,2,4,2,32,5,6,7,8,4,0,2,4,5,3,5,3,2,1,2,3,4,5,6,3,4,7,8,4,6,6,5,4,3,54,3,5,2,6,7,6]
print(s.candy(s1) == 159)