class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        @cache
        def solve(i,j):
            if i >= n or j >= m: return 0

            ans = 0
            if text1[i] == text2[j]:
                ans = 1 + solve(i+1, j+1)
            else:
                cond1 = solve(i+1,j)
                cond2 = solve(i, j+1)
                ans = max(cond1, cond2)
            return ans
        return solve(0,0)
            
        
        
        
        
        
        
        
        
        
        # n = len(text1)
        # m = len(text2)

        # dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # for i in reversed(range(m)):
        #     for j in reversed(range(n)):
        #         if text2[i]==text1[j]:
        #             dp[j][i] = 1 + dp[j+1][i+1]
        #         else:
        #             dp[j][i] = max(dp[j+1][i],dp[j][i+1])
        # return dp[0][0]

        

# top down dp
# def solve(i,j):
        #     if i>=n or j>=m: return 0
        #     if dp[i][j]!=-1: return dp[i][j]

        #     ans = 0
        #     if text1[i]==text2[j]:
        #         ans = 1 + solve(i+1,j+1)
        #     else:
        #         cond1 = solve(i+1,j)
        #         cond2 = solve(i,j+1)
        #         ans = max(cond1,cond2)
        #     dp[i][j] = ans
        #     return dp[i][j]
        # return solve(0,0)
