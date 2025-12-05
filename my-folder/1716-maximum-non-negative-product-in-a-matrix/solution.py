class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 10**9 + 7
        max_ans = -1

        @cache
        def dp(i,j, prod):
            nonlocal max_ans
            if i == n - 1  and j == m - 1:
                if ( prod * grid[i][j] ) >= 0:
                    max_ans = max(max_ans, ( prod * grid[i][j]) )
                    return True
                else: return False
            
            if (i > n or j > m) or ( i != n and j == m) or (i == n and j!=m):
                return False
            
            curr = grid[i][j]
            right, down = dp(i, j+1, (prod * curr)), dp(i+1, j, ( prod * curr) )
            return right or down

        ans = dp(0, 0, 1)
        if ans:
            return max_ans % MOD
        else:
            return -1
