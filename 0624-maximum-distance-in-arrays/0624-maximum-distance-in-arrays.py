class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max1 = max((arrays[0][-1], 0), (arrays[1][-1], 1))
        min1 = min((arrays[0][0], 0), (arrays[1][0], 1))
        
        max2 = (arrays[abs(max1[1] - 1)][-1], abs(max1[1] - 1))
        min2 = (arrays[abs(min1[1] - 1)][0], abs(min1[1] - 1))
        
        for i in range(2, len(arrays)):
            array = arrays[i]
            v = (array[-1], i)
            max2 = max(max2, v)
            if max2 > max1:
                temp = max1
                max1 = max2
                max2 = temp
            
            v = (array[0], i)
            min2 = min(min2, v)
            if min2 < min1:
                temp = min1
                min1 = min2
                min2 = temp
        
        if min1[1] == max1[1]:
            return max(abs(max1[0] - min2[0]), abs(max2[0] - min1[0]))
        return abs(max1[0] - min1[0])