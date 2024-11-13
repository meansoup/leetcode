class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        result = 0
        
        nums.sort()
        for i in range(len(nums)):
            lower_huddle = self.bin_big(nums, i, lower - nums[i])
            upper_huddle = self.bin_small(nums, i, upper - nums[i])
            if lower_huddle <= upper_huddle:
                result += upper_huddle - lower_huddle + 1
                
        return result 
            
        
    def bin_big(self, nums, base, target_num):
        result = len(nums)
        
        head = base + 1
        tail = len(nums)
        
        while head < tail:
            mid = (head + tail) // 2
            
            if nums[mid] == target_num:
                tail = mid
                result = mid
            if nums[mid] < target_num:
                head = mid + 1
            elif nums[mid] > target_num:
                tail = mid
                result = mid
        return result
        
    def bin_small(self, nums, base, target_num):
        result = base
        
        head = base
        tail = len(nums)
        
        while head < tail:
            mid = (head + tail) // 2
            
            if nums[mid] == target_num:
                result = mid
                head = mid + 1
            if nums[mid] < target_num:
                result = mid
                head = mid + 1
            elif nums[mid] > target_num:
                tail = mid
        return result
        