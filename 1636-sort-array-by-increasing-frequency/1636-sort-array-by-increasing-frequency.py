class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_freq = {}
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 0                
            num_freq[num] += 1
                
        sorted_num_freq = dict(sorted(num_freq.items(), key=lambda item: (item[1], -item[0])))
        
        result = []
        for k in sorted_num_freq:
            result.extend([k] * sorted_num_freq[k])

        return result