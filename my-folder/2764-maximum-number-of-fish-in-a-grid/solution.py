class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0

            fish = grid[x][y]
            grid[x][y] = 0 

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in directions:
                fish += dfs(x + dx, y + dy)

            return fish

        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0: 
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish
