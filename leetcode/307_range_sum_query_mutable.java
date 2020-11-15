class NumArray {
    public int[] nums;
    public int[] blocks;
    public int blocklen;

    public NumArray(int[] nums) {
        this.nums = nums;
        double l = Math.sqrt(nums.length);
        blocklen = (int) Math.ceil(nums.length / l);
        blocks = new int[blocklen];
        for (int i=0; i < nums.length; i++) {
            blocks[i/blocklen] += nums[i];
        }
    }
    
    public void update(int i, int val) {
        int blocki = i / blocklen;
        blocks[blocki] += val - nums[i];
        nums[i] = val;
    }
    
    public int sumRange(int i, int j) {
        int s= 0;
        int startblock = i / blocklen,
            endblock = j / blocklen;
        
        if (endblock == startblock) {
            for (int b = i; b <= j; b++)
                s += nums[b];
        } else {
            for (int b = i; b <= (startblock + 1) * blocklen -1; b++) {
                s += nums[b];
            }
            for (int b = startblock + 1; b <= endblock -1; b++) {
                s += blocks[b];
            }
            for (int b = endblock * blocklen; b <= j; b++) {
                s += nums[b];
            }
        }
                
        return s;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */