class Solution {
    private int result = 0;
    
    public int findTargetSumWays(int[] nums, int target) {
        internal(nums, target, 0);
        return result;
    }
    
    private void internal(int[] nums, int target, int i) {
        if (i == nums.length) {
            if (target == 0) {
                result++;
            }
            return;
        }
        
        internal(nums, target + nums[i], i + 1);
        internal(nums, target - nums[i], i + 1);
    }
}