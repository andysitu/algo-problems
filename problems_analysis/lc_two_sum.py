import List
"""
Brute force approach: n^2 runtime, constant space
Search through all the values
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

"""
Use dictionary to save results of the integers since you need
2 integers and you already know the target, so you can search
if there is a value in the dictionary in constant time
Runtime: O(n); Space: O(n)
"""
def twoSum2(self, nums: List[int], target: int) -> List[int]:
    nmap = {}
    for i in range(len(nums)):
        if nums[i] not in nmap:
            nmap[nums[i]] = [i,]
        else:
            nmap[nums[i]].append(i)
    for i in range(len(nums)-1):
        if target - nums[i] in nmap:
            for index in nmap[target-nums[i]]:
                if index != i:
                    return [i, index]

"""
Other approaches:
Best runtime is O(n) since you have to read each value at least once
The only improvement might be the space complexity. You could
throw away values that would never reach target and not put in the values
with duplicates since if there is a duplicate indices, you can test 
if it reaches the target right on the spot.
"""