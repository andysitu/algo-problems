class Solution:
    def threeSum(self, nums):
        sols = []
        _2mult = {}
        # ensures that 3 values are sorted
        nums.sort()
        s = set(nums)
        l = len(nums)
        if l < 3:
            return []
        max = nums[l-1]
        min = nums[0]

        for i in range(1,l-1):
            for j in range(i+1, l):
                v = nums[i] + nums[j]
                vneg = v * -1
                if vneg not in s:
                    continue
                if vneg > max:
                    continue
                if vneg < min:
                    break
                if v not in _2mult:
                    _2mult[v] = [{
                    "k1": i, "k2": j}]
                else:
                    _2mult[v].append({
                        "k1": i, "k2": j})
        values = {}
        for i in range(l):
            n = nums[i] * -1
            if n in _2mult:
                l1 = len(_2mult[n])
                for j in range(l1):
                    d = _2mult[n][j]
                    if i < d["k1"]:
                        s = str(nums[i]) + "_" + str(nums[d["k1"]]) + "_" + str(nums[d["k2"]])
                        values[s] = True
        for k in values:
            sols.append([int(n) for n in k.split("_")])
        
        return sols