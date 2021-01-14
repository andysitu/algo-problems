class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow