class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int i=0; i < nums.length; i++) {
            while (nums[nums[i]-1] != nums[i] && nums[i] != i+1) {
                int n = nums[i];
                nums[i] = nums[n - 1];
                nums[n-1] = n;
            }
        }
        List<Integer> ans = new ArrayList<Integer>();
        for (int i=0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                ans.add(i+1);
            }
        }
        return ans;
    }
}