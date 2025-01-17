class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def solve(i,total):
            if i>=n:return float('inf')
            if total>amount: return float('inf')

            if total==amount:return 0
            take = 1 + solve(i,total+coins[i])
            not_take = solve(i+1,total)
            return min(take,not_take)
        out = solve(0,0)
        return -1 if out==float('inf') else out

