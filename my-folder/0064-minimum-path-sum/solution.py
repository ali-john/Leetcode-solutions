class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        memo = {}
        def dp(i,j):
            if i<0 or i>=n or j<0 or j>=m: return float('inf')
            if i==n-1 and j==m-1: return grid[i][j]
            if (i,j) in memo: return memo[(i,j)]

            right = grid[i][j] + dp(i,j+1)
            down = grid[i][j] + dp(i+1,j)
            memo[(i,j)] = min(right,down)
            return memo[(i,j)]
        return dp(0,0)
