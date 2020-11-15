from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)

        ratingtup = []

        for i in range(len(ratings)):
            ratingtup.append((ratings[i], i))

        ratingtup= sorted(ratingtup, key=lambda ratingtup: ratingtup[0])

        for i in range(len(ratings)):
            actual_index = ratingtup[i][1]
            if actual_index > 0 and ratings[actual_index] > ratings[actual_index -1] \
                and candy[actual_index] <= candy[actual_index - 1]:
                candy[actual_index] = candy[actual_index - 1] + 1
            if actual_index < len(ratings)-1 and ratings[actual_index] > ratings[actual_index + 1] \
                and candy[actual_index] <= candy[actual_index +1]:
                candy[actual_index] = candy[actual_index +1] + 1

        # print(ratingtup)
        # print(candy)

        sumcandy = 0
        for x in candy:
            sumcandy += x
        return sumcandy

s = Solution()
print(s.candy([1,0,2]))
print(s.candy([2,4,5,2,1,1,2,3,2,2,1,2,3,4]))
print(s.candy([]))
print(s.candy([1,2,2]))
s1 = [1,0,3,4,2,1,3,2,4,2,3,1,2,3,4,5,6,24,2,3,4,1,2,3,2,4,1,2,4,2,32,5,6,7,8,4,0,2,4,5,3,5,3,2,1,2,3,4,5,6,3,4,7,8,4,6,6,5,4,3,54,3,5,2,6,7,6]
print(s.candy(s1) == 159)