class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        max_cnt = 0
        head, tail, cost, cnt = 0, 0, 0, 0
        while tail < len(t):
            if cost + diff[tail] <= maxCost:
                cost += diff[tail]
                tail += 1
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cost -= diff[head]
                head += 1
                cnt -= 1

        return max_cnt