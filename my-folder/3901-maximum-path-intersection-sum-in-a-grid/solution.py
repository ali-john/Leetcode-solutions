class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = float("-inf")
        for i in range(1, n-1):
            for j in range(1, m-1):
                ans = max(ans, grid[i][j])
        
        # check rows
        for i in range(n):
            curr = grid[i][0]
            for j in range(1,m):
                curr = max(curr+grid[i][j], grid[i][j] + grid[i][j-1])
                ans = max(ans, curr)
        # check columns
        for j in range(m):
            curr = grid[0][j]
            for i in range(1,n):
                curr = max(curr + grid[i][j], grid[i][j] + grid[i-1][j])
                ans = max(ans, curr)
        return ans
