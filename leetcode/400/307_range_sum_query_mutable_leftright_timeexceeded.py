class NumArray:

    def __init__(self, nums: List[int]):
        self.nlen = len(nums)
        if self.nlen == 0:
            return
        
        self.nums = nums
        
        self.left = []
        s=0
        for n in nums:
            s += n
            self.left.append(s) 
        
        self.right = [0] * self.nlen
        s=0
        for i in range(self.nlen-1, -1, -1):
            s += nums[i]
            self.right[i] = s
        self.total = self.left[self.nlen-1]
        

    def update(self, i: int, val: int) -> None:
        prev = self.nums[i]
        self.nums[i] = val
        
        for j in range(i, self.nlen):
            self.left[j] += val - prev
            
        for j in range(i, -1, -1):
            self.right[j] += val - prev
        self.total += val - prev
        
    def sumRange(self, i: int, j: int) -> int:
        if self.nlen == 0:
            return 0
        s = self.total
        if i > 0:
            s -= self.left[i-1]
        if j < self.nlen-1:
            s -= self.right[j+1]
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)