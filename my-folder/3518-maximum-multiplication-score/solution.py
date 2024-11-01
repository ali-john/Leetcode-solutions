class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        mx = -10000000000000
        dp = [[mx for _ in range(len(b)+10)] for _ in range(5)]

        def solve(i,j):
            if i>=len(a):
                return 0
            if j>=len(b):
                return mx
            if dp[i][j]!=mx:
                return dp[i][j]
            # dont take
            dt = solve(i,j+1)
            #take
            t = solve(i+1,j+1) + (a[i]*b[j])
            result = max(dt,t)
            dp[i][j] = result
            return dp[i][j]
        return solve(0,0)
