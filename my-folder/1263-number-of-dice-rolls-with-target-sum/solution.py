class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        memo = {}
        def dp(rem, curr_sum):
            if (rem,curr_sum) in memo:
                return memo[(rem, curr_sum)]
            
            if rem < 0 or curr_sum > target:
                return 0
            
            if rem == 0 and curr_sum == target:
                return 1
            
            ans = 0
            for state in range(1, k+1):
                ans+= dp(rem - 1, curr_sum + state)
            
            memo[(rem, curr_sum)] = ans % MOD
            return memo[(rem, curr_sum)]
        
        return dp(n, 0)
        

        

