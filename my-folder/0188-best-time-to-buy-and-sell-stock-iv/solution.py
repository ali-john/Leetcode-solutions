class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def dp(i,transactions,holding):
            if i>=n or transactions==0:
                return 0
            
            if (i,transactions,holding) in memo:
                return memo[(i,transactions,holding)]

            do_nothing = dp(i+1,transactions,holding)
            do_something = 0
            if holding:
                # we can sell the stock
                do_something = prices[i] + dp(i+1,transactions-1,0)
            else:
                # buy new stock
                do_something = -prices[i] + dp(i+1,transactions,1)
            memo[(i,transactions,holding)] = max(do_nothing,do_something)
            return memo[(i,transactions,holding)]
        
        return dp(0,k,0)

