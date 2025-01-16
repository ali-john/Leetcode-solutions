class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        def solve(i,j):
            if i>=n or j>=m: return 0

            if dp[i][j]!=-1: return dp[i][j]
            
            dp[i][j] = 0
            right = solve(i,j+1)
            down = solve(i+1,j)
            diag = solve(i+1,j+1)
            if grid[i][j] == '1':
                dp[i][j] = 1 + min(right,down,diag)
            return dp[i][j]
        solve(0,0)
        max_area = 0
        for i in range(n):
            for j in range(m):
                max_area = max(max_area,dp[i][j])
        return max_area**2
            
