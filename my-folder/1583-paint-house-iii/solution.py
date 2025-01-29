from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        memo = {}

        def dp(i, color, t):
            if t > target: 
                return float('inf')
            if i == m: 
                return 0 if t == target else float('inf')
            if (i, color, t) in memo: 
                return memo[(i, color, t)]

            if houses[i] == 0: # house not painted yet 
                min_cost = float('inf')
                # continue neighbourhood
                min_cost = min(min_cost, cost[i][color] + dp(i + 1, color, t))
                for c in range(n):
                    if c == color:
                        continue
                    min_cost = min(min_cost, cost[i][c] + dp(i + 1, c, t + 1))
            else: 
                if houses[i] - 1 == color:
                    min_cost = dp(i + 1, color, t)
                else: 
                    min_cost = dp(i + 1, houses[i] - 1, t + 1)

            memo[(i, color, t)] = min_cost
            return min_cost
        
        ans = float('inf')
        for color in range(n):
            if houses[0] == 0:
                ans = min(ans, cost[0][color] + dp(1, color, 1))
            elif houses[0] - 1 == color:
                ans = min(ans, dp(1, color, 1))
        
        return ans if ans != float('inf') else -1 

