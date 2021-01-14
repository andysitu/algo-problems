class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ndict = {}
        for i in range(len(numbers)):
            if numbers[i] in ndict and numbers[i] * 2 == target:
                return [ ndict[numbers[i]]+1, i+1]
            ndict[numbers[i]] = i

        for i in range(len(numbers)):
            if (target - numbers[i]) in ndict:

                if ndict[target - numbers[i]] > i:
                    return [i+1, ndict[target - numbers[i]]+1]
                else:
                    return [ndict[target - numbers[i]]+1, i+1]