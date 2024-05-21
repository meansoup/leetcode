import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            copied_subsets = copy.deepcopy(subsets)
            for subset in copied_subsets:
                subset.append(num)
            subsets.extend(copied_subsets)
            
        return subsets