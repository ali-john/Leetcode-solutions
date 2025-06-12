class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:


        n = len(prices)
        INF = -inf
        dp = [ [ [INF]*3 for _ in range(k+1)] for _ in range(n+1)]

        def f(i,t,state):
            if i == n:
                if state == 0:
                    return 0
                else:
                    return INF
            if dp[i][t][state]!=INF:
                return dp[i][t][state]
            
            profit = INF
            profit = max(profit, f(i+1,t, state) )

            if state == 0: # new beginining
                # hold a long trans
                profit = max(profit , -prices[i] + f(i+1,t,1) )
                # hold a short trans
                profit = max(profit, prices[i] + f(i+1, t, 2))
            
            elif t > 0:
                if state == 1: 
                    # complete trans
                    profit = max(profit, prices[i] + f(i+1,t -1, 0))
                else:
                    profit = max(profit, -prices[i] + f(i+1, t -1, 0))
            
            dp[i][t][state] = profit
            return profit
        return f(0,k,0)

