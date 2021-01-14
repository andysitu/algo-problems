class Solution:
    def fourSum(self, nums, target):
        sums = {}
        l = len(nums)
        if l <= 3:
            return []
        for i in range(l):
            for j in range(i+1, l):
                sum = nums[i] + nums[j]
                if sum not in sums:
                    sums[sum] = []
                sums[sum].append({
                    "sum": sum,
                    "i": i,
                    "j": j
                })

        sol = []
        record = {} # Record Numbers used already
        # Find the corresponding sums to produce target
        sums_key = list(sums.keys())
        l_sums = len(sums_key)
        for i in range(l_sums):
            sum1 = sums_key[i]
            sum2 = target - sum1
            if sum2 in sums:
                for s1 in sums[sum1]:
                    for s2 in sums[sum2]:
                        if s1["i"] == s2["i"] or s1["j"] == s2["j"] or s1["i"] == s2["j"] or s1["j"] == s2["i"]:
                            continue
                        else:
                            psol = [
                                nums[s1["i"]],
                                nums[s1["j"]],
                                nums[s2["i"]],
                                nums[s2["j"]],
                            ]
                            psol.sort()
                            slstr = ""
                            for i in psol:
                                slstr += str(i)
                            if slstr not in record:
                                sol.append(psol)
                                record[slstr] = True
        return sol


s = Solution()
print(s.fourSum( [1, 0, -1, 0, -2, 2], 0))