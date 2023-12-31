class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                count += len(grid[i])
                continue
            for j in range(len(grid[i]) - 1, -1, -1):
                if grid[i][j] < 0:
                    count += 1
                else:
                    break
        return count