import time

class Solution:
    def threeSum(self, nums):
        sols = []
        _2mult = {}
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                v = nums[i] + nums[j]
                if v not in _2mult:
                    _2mult[v] = []
                _2mult[v].append(str(i) + "_" + str(j))
        d = {}
        for i in range(l):
            n = nums[i] * -1
            if n in _2mult:
                l1 = len(_2mult[n])
                for j in range(l1):
                    ind_str = _2mult[n][j]
                    a = ind_str.split("_")
                    exit_status = False
                    for k in range(2):
                        g = int(a[k])
                        if i == g:
                            exit_status = True
                            break
                        a[k] = g
                    if exit_status:
                        continue
                    a.append(i)
                    # convert to values
                    for k in range(3):
                        v = a[k]
                        a[k] = str(nums[v])
                    a.sort()
                    s = "_".join(a)
                    d[s] = True
        for k in d:
            sols.append([int(n) for n in k.split("_")])
        return sols