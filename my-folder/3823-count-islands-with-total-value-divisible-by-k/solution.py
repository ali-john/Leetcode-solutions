class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if i >=m or i<0 or j>=n or j<0 or grid[i][j] <= 0: return 0

            val = grid[i][j]
            grid[i][j] = -1
            return val + (
                dfs(i+1, j) + 
                dfs(i-1, j) + 
                dfs(i, j+1) + 
                dfs(i, j - 1) 
            )
            

            
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    s = dfs(i,j)
                    if s%k == 0: ans+=1
        return ans
        



