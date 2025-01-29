class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        memo = {}

        def dp(i,color):
            if i>=n: return 0
            if (i,color) in memo: return memo[(i,color)]

            total_cost = costs[i][color]
            other = float('inf')
            for c in range(k):
                if c!=color:
                    other = min(dp(i+1,c),other)
            total_cost+=other
            memo[(i,color)] = total_cost
            return memo[(i,color)]
        ans = float('inf')

        for i in range(k):
            ans = min(ans,dp(0,i))
        return ans
