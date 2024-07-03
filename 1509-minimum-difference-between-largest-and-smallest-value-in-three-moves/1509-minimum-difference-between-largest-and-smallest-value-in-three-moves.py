class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        nums.sort()
        
        return min(nums[N - 1] - nums[3], nums[N - 2] - nums[2], nums[N - 3] - nums[1], nums[N - 4] - nums[0])
        
