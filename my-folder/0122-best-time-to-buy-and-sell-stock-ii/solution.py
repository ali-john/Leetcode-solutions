class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        memo = {}
        def dp(i,lock):
            if i >=n:
                return 0
            
            if (i,lock) in memo: return memo[(i,lock)]
            do_nothing = dp(i+1,lock)
            do_something = 0

            if lock: # sell the stock
                do_something = prices[i] + dp(i+1,0)
            else: # buy stock
                do_something = -prices[i] + dp(i+1,1)
            
            memo[(i,lock)] = max(do_nothing, do_something)
            return memo[(i,lock)]
        
        return dp(0,0)
        
               


