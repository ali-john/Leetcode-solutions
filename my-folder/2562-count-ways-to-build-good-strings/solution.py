class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(length):
            if length > high:
                return 0
            
            count = 1 if length >= low else 0
            count += dp(length + zero) + dp(length + one) % MOD

            return count % MOD
        
        return dp(0)
