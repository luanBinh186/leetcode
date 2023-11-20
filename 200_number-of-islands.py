class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_island = 0
        def dfs(grid: List[List[str]], i: int, j: int):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] != '0':
                grid[i][j] = '0'
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    total_island += 1
        return total_island