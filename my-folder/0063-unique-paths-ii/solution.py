class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        memo = {}
        def dp(i,j):
            if i<0 or i>=n or j<0 or j>=m: return 0
            if grid[i][j] == 1: return 0
            if i==n-1 and j==m-1:return 1
            if (i,j) in memo: return memo[(i,j)]
            
            down = dp(i+1,j)
            up = dp(i,j+1)
            memo[(i,j)] = down+up
            return memo[(i,j)]
        return dp(0,0)
