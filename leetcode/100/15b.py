class Solution:
    def threeSum(self, nums):
        sols = []
        _2mult = {}
        l = len(nums)
        # ensures that 3 values are sorted
        nums.sort()
        s = {}
        for i in range(l):
            s[nums[i]] = i
        max = nums[l-1]
        min = nums[0]
        values = {}

        for i in range(1,l-1):
            for j in range(i+1, l):
                v = nums[i] + nums[j]
                vneg = v * -1
                if vneg > max:
                    continue
                if vneg < min:
                    break
                if vneg in s:
                    vk = s[vneg]
                    if vk < i:
                        st = str(nums[vk]) + "_" + str(nums[i]) + "_" + str(nums[j])
                        values[st] = True
        
        for k in values:
            sols.append([int(n) for n in k.split("_")])
        
        return sols