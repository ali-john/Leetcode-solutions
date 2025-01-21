class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        memo = {}
        def dp(i,total):
            if i>=n: return 0
            if total>amount: return 0

            if total==amount: return 1

            if (i,total) in memo: return memo[(i,total)]
            take = dp(i,total+coins[i])
            dont_take = dp(i+1,total)

            memo[(i,total)] = take + dont_take
            return memo[(i,total)]
        return dp(0,0)
        
