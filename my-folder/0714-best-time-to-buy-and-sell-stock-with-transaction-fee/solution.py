class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}

        def dp(i,holding):
            if i>=n: return 0
            if (i,holding) in memo: return memo[(i,holding)]

            # do nothing -> go to next stock
            do_nothing = dp(i+1,holding)

            # do something
            do_something = 0
            if holding: # sell the stock
                do_something = -fee + prices[i] + dp(i+1,0)
            else: # buy stock
                do_something = -prices[i] + dp(i+1,1)
            memo[(i,holding)] = max(do_nothing,do_something)
            return memo[(i,holding)]
        return dp(0,0)





