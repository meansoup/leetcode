class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit = [0] * 30
        
        for c in candidates:
            i = 0
            while c > 0:
                if c % 2 == 1:
                    bit[i] += 1
                c = c // 2
                i += 1
            
        return max(bit)
                
                
            