class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ns = set()
        for i in range(len(nums)):
            if nums[i] in ns:
                return True
            ns.add(nums[i])
        return False