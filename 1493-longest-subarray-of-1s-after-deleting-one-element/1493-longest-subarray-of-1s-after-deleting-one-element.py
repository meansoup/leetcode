class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        before = 0
        cur = 0
        
        for i in nums:
            if i == 1:
                cur += 1
                max_len = max(max_len, before + cur)
            else:
                before = cur
                cur = 0

        if len(nums) == max_len:
            max_len -= 1
            
        return max_len
            
        