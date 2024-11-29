class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 10001;
        }
        
        dp[0] = 0;
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < i + nums[i] + 1; j++) {
                if (j >= nums.length) {
                    break;
                }
                
                dp[j] = Math.min(dp[j], dp[i] + 1);                
            }
        }
        
        return dp[nums.length - 1];
    }
}

