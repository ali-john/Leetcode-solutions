class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        memo = {}

        def dp(i,color):
            if i>=n: return 0
            if (i,color) in memo: return memo[(i,color)]

            cost = float('inf')
            zero_cost_one = zero_cost_two = one_cost_zero = one_cost_two = two_cost_zero = two_cost_one = float('inf')
            if color==0: # paint with 1 and 2
                zero_cost_one = costs[i][1] + dp(i+1,1)
                zero_cost_two = costs[i][2] + dp(i+1,2)
            elif color == 1: # paint with 0 and two
                one_cost_zero = costs[i][0] + dp(i+1,0)
                one_cost_two = costs[i][2] + dp(i+1,2)
            elif color == 2: # paint with 0 and 1
                two_cost_zero = costs[i][0] + dp(i+1,0)
                two_cost_one = costs[i][1] + dp(i+1,1)
            
            memo[(i,color)] = min(zero_cost_one, zero_cost_two, one_cost_zero, one_cost_two, two_cost_zero, two_cost_one)
            return memo[(i,color)]
        return min(dp(0,0), dp(0,1), dp(0,2) )


