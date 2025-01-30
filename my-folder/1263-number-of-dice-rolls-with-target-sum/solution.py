class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        memo = {}
        def solve(rem,s):
            if rem<0 or s>target: return 0
            if (rem,s) in memo: return memo[(rem,s)]

            if rem==0 and s==target: return 1
            ans = 0
            for i in range(1,k+1):
                ans+=solve(rem-1,s+i)
            memo[(rem,s)] = ans % MOD
            return memo[(rem,s)]
        return solve(n,0) % MOD

