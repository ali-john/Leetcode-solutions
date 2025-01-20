class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        n = len(cost)
        # def dp(i):
        #     if i<=1: return 0
        #     if i in memo: return memo[i]
        #     one_step = cost[i-1] + dp(i-1)
        #     two_step = cost[i-2] + dp(i-2)
        #     memo[i] = min(one_step,two_step)
        #     return memo[i]
        # return dp(n)

        dp = [0]*(n+1)
        
        for i in range(2,n+1):
            one_step = cost[i-1] + dp[i-1]
            two_step = cost[i-2] + dp[i-2]
            dp[i] = min(one_step,two_step)
        return dp[-1]




