import heapq
from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        n = len(grid)
        m = len(grid[0])

        @cache
        def dp(i,j, curr):
            if i >= n or j >=m:
                return float('-inf')
            
            score, cost = 0, 0
            if grid[i][j] == 0:
                score, cost = 0, 0
            if grid[i][j] == 1:
                score, cost = 1, 1
            if grid[i][j] == 2:
                score, cost = 2, 1
            
            if curr + cost > k:
                return float('-inf')
            
            if i == n - 1 and j == m - 1:
                if curr > k:
                    return float('-inf')
                return score
            
            op1 = dp(i+1, j, curr + cost)
            op2 = dp(i, j+1, curr + cost)

            ans = max(op1, op2)
            return score + ans
        ans = dp(0,0,0)
        if ans == float('-inf'):
            return -1
        return ans

        

