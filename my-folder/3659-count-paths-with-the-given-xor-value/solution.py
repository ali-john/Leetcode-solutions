class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        dp = [[[-1]*16 for _ in range(m)] for _ in range(n)]
        
        def solve(i, j, path_xor):
            path_xor ^= grid[i][j]
            
            if i == n-1 and j == m-1:
                return 1 if path_xor == k else 0
            
            if dp[i][j][path_xor] != -1:
                return dp[i][j][path_xor]
            
            res = 0
            if i + 1 < n:
                res += solve(i+1, j, path_xor)
            if j + 1 < m:
                res += solve(i, j+1, path_xor)
            
            dp[i][j][path_xor] = res % MOD
            return dp[i][j][path_xor]
        
        return solve(0, 0, 0)
