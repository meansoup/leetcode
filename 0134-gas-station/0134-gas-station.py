class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [gas[i] - cost[i] for i in range(len(gas))]
        
        mini = 0
        for i in range(1, len(gas)):
            remain[i] += remain[i - 1]
            if remain[i] <= remain[mini]:
                mini = i
        
        result = self.next(len(gas), mini)
        
        avb = 0
        for i in range(len(remain)):
            nextt = self.next(len(gas), result + i -1)
            avb += gas[nextt] - cost[nextt]
            if avb < 0:
                return -1
                
        return result
        
    def next(self, size, n):
        if n < size - 1:
            return n + 1
        else:
            return n - (size - 1)