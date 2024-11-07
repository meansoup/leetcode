class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        min_of_segment = nums[0]
        max_of_segment = nums[0]
        prev_bits = bin(nums[0]).count("1")
        
        max_of_prev_segment = 0
        
        
        for num in nums:
            print(num)
            if bin(num).count("1") == prev_bits:
                min_of_segment = min(min_of_segment, num)
                max_of_segment = max(max_of_segment, num)
            else:
                if min_of_segment < max_of_prev_segment:
                    return False
                
                max_of_prev_segment = max_of_segment
                
                min_of_segment = num
                max_of_segment = num

                prev_bits = bin(num).count("1")
                
        if min_of_segment < max_of_prev_segment:
            return False
                
        return True