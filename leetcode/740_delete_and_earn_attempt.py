class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        values = {}
        lost = []
        for n in nums:
            if n not in values:
                values[n] = n
            else:
                values[n] += n
        for n in values:
            l = 0
            if n+1 in values:
                l += values[n+1]
            if n-1 in values:
                l += values[n-1]
            lost.append([l, n])
        lost.sort(key=lambda x: x[0])
        print(lost)
        print(values)
        value = 0
        for l in lost:
            if values[l[1]] != -1:
                value += values[l[1]]
                if l[1] + 1 in values:
                    values[l[1] + 1] = -1
                if l[1] -1 in values:
                    values[l[1] -1] = -1
        return value