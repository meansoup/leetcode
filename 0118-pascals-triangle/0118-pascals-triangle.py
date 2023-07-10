pascal = [[1], [1, 1]]
for i in range(1, 29):
    idx = pascal[i]
    pascal.append([a + b for a, b in zip(idx + [0], [0] + idx)])

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        return [pascal[i] for i in range(0, numRows)]
