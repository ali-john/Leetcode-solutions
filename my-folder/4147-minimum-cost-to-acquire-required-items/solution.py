class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth > cost1 + cost2:
            return (cost1 * need1) + (cost2 * need2)
        
        if need1 == 0 and need2 == 0:
            return 0
        
        possible = [0, need1, need2, min(need1, need2), max(need1, need2)]

        ans = float('inf')
        for k in possible:
            cost = (k*costBoth) + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2
            ans = min(cost, ans)
        return ans
