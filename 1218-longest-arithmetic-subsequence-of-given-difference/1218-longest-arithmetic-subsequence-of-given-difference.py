class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        length = {}
        max_length = 0
        
        for i in arr:
            length[i] = length.get(i - difference, 0) + 1
            max_length = max(length[i], max_length)
            
        return max_length