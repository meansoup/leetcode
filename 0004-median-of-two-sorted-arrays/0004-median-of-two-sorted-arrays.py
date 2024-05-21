class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        tm, tn = 0, 0
        ex, cur = 0, 0
        while tm + tn < (m + n) // 2 + 1:
            ex = cur
            if tn >= n or (tm < m and nums1[tm] < nums2[tn]):
                cur = nums1[tm]
                tm += 1
            else:
                cur = nums2[tn]
                tn += 1
        
        return cur if (m + n) % 2 == 1 else (ex + cur) / 2
        
        