class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nums = [0] * 1001
        for num in arr1:
            nums[num] += 1
        result = []
        for num in arr2:
            result.extend([num] * nums[num])
            nums[num] = 0
        for i in range(len(nums)):
            result.extend([i] * nums[i])
        return result