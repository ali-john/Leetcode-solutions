class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        memo = {}
        def dp(i):
            if i==1:return k
            if i==2: return k*k

            if i in memo: return memo[i]
            different = (k-1)*dp(i-1)
            same = 1*(k-1)*dp(i-2)
            memo[i] = same + different
            return memo[i]
        return dp(n)
