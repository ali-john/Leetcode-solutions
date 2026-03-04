class Solution:
    def minCost(self, n: int) -> int:

        @cache
        def dp(num):
            if num == 1:
                return 0
            if num == 2:
                return 1

            cost = dp(num - 1) + (num - 1)
            return cost

        return dp(n)
            
                
            
