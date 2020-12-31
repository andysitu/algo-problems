class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        values = {}
        for n in nums:
            if n not in values:
                values[n] = n
            else:
                values[n] += n
        keys = []
        for n in values:
            keys.append(n)
        keys.sort()
        klen = len(keys)
        if klen == 1:
            return values[keys[-1]]
        for i in range(klen-2, -1, -1):
            n = keys[i]
            if n+1 in values:
                if n+2 in values and n+3 in values:
                    values[n] += max(values[n+2], values[n+3])
                elif i < klen -3:
                    values[n] += max(values[keys[i+2]], values[keys[i+3]])
                elif i < klen - 2:
                    values[n] += values[keys[i+2]]
            else:
                if i < klen -2:
                    values[n] += max(values[keys[i+1]], values[keys[i+2]])
                else:
                    values[n] += values[keys[i+1]]
        if klen >= 3:
            return max(values[keys[0]], values[keys[1]], values[keys[2]])
        else:
            return max(values[keys[0]], values[keys[1]])