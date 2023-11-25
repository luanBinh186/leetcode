class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rs = [0]
        def dfs(grid: List[List[int]], i: int, j: int) -> int:
            total = 0
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
                total += 1
                grid[i][j] = 0
                total += dfs(grid, i + 1, j)
                total += dfs(grid, i - 1, j)
                total += dfs(grid, i, j + 1)
                total += dfs(grid, i, j - 1)
            return total
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                t = dfs(grid, i, j)
                if t > 0:
                    rs.append(t)
        return max(rs) 