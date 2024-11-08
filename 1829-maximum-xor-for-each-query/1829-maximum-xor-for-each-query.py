class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maximum = pow(2, maximumBit) - 1
        result = []
        
        ex = nums[0] ^ maximum
        result.append(ex)
        
        for num in nums[1:]:
            ex = num ^ ex
            result.append(ex)
            
        return result[::-1]
            
        