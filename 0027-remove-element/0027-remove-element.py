class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_idxs = []
        for i in range(len(nums)):
            if nums[i] == val:
                val_idxs.append(i)

        tail = len(nums) - 1
        for i in val_idxs:
            if nums[i] == -1:
                break
            while tail >= 0 and (nums[tail] == val or nums[tail] == -1):
                nums[tail] = -1
                tail -= 1
            if tail < i:
                break
            nums[i] = nums[tail]
            nums[tail] = -1
            
        return len(nums) - len(val_idxs)
                