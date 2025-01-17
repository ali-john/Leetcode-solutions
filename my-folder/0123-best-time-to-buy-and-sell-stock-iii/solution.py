class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        memo = {}
        def dp(i,trans,holding):
            if i>=n or trans>=2:
                return 0
            
            if (i,trans,holding) in memo: return memo[(i,trans,holding)]

            do_nothing = dp(i+1,trans,holding)
            do_something = 0
            if holding: # sell stock
                do_something = prices[i] + dp(i+1,trans+1,0)
            else: # buy stock
                do_something = -prices[i] + dp(i+1,trans,1)
            
            memo[(i,trans,holding)] = max(do_nothing,do_something)
            return memo[(i,trans,holding)]
        
        return dp(0,0,0)
