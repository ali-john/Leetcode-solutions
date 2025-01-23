class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]





        # ------------ Top - Down dp---------------------------------
        # memo = {}
        # def dp(i,j):
        #     if i<0 or i>=n or j<0 or j>=m: return 0
        #     if i==n-1 and j==m-1: return 1
        #     if (i,j) in memo: return memo[(i,j)]

        #     down = dp(i+1,j)
        #     right = dp(i,j+1)
        #     memo[(i,j)] = down+right
        #     return memo[(i,j)]
        # return dp(0,0)

