class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_mod = 0
        mod_seen = {0: 1}
        result = 0

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in mod_seen:
                result += mod_seen[prefix_mod]
            else:
                mod_seen[prefix_mod] = 0
            mod_seen[prefix_mod] += 1

        return result