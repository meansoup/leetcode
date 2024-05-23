class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        sublists = [[nums[0]]]
        for num in nums[1:]:
            not_beautiful_low = num - k
            not_beautiful_high = num + k
            sublists.extend([sublist + [num] for sublist in sublists if not_beautiful_high not in sublist and not_beautiful_low not in sublist])
            sublists.append([num])

        return len(sublists)