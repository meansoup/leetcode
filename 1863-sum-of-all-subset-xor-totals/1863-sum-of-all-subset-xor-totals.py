import copy

class Solution:
    def __init__(self):
        self.xors = []

    def xor(self, list):
        result = 0
        for value in list:
            result ^= value
        return result

    def subsetXORSum(self, nums: list[int]) -> int:
        subsets = [[]]

        for num in nums:
            copied_subsets = copy.deepcopy(subsets)
            for subset in copied_subsets:
                subset.append(num)
                xor_result = self.xor(subset)
                self.xors.append(xor_result)
            subsets.extend(copied_subsets)

        return sum(self.xors)
