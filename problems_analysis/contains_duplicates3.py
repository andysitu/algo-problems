"""
Given an array of integers, find out whether there are two distinct 
indices i and j in the array such that the absolute difference 
between nums[i] and nums[j] is at most t and the absolute difference 
between i and j is at most k.
Runtime: O(n^2) ; space: O(1)
"""

"""
Brute force:
2 for loops and for each n you search all the numbers ahead of it within k
to see if the difference is within t
runtime: O(n^2) ; space: O(1)
"""

"""
Save the values in a bin by dividing n / t and using a dictionary to save this
as the key while the actual number os the value
For each n, search in the bin for value b (n/t), b-1, and b+1
For each of the 3, manually check if the difference is within t

finally remove the number at i-k
Runtime: O(n); space: O(k) or n if it's smaller
"""

def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    nmap = {}
    for i in range(len(nums)):
        u = 1 if t == 0 else t
        n = nums[i] // u
        if n in nmap:
            return True
        if n - 1 in nmap  and abs(nums[i] - nmap[n-1])  <= t:
            return True
        if n + 1 in nmap and abs(nums[i] - nmap[n+1]) <= t:
            return True

        if i >= k:
            del nmap[nums[i-k] // t]
    return False