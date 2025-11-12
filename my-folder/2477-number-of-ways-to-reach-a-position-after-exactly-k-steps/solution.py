class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(pos, k):
            if k == 0:
                if pos == endPos:
                    return 1
                return 0
            negative = dp(pos -1, k-1)%MOD
            positive = dp(pos + 1, k - 1) % MOD
            return ( negative + positive ) % MOD
        return dp(startPos, k) % MOD
