class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        memo = {}
        def dp(r1,c1, r2, c2):
            
            if (r1,c1,r2,c2) in memo:
                return memo[(r1,c1,r2,c2)]
            
            # if it is 1x1 now
            if r1 == r2 and c1 == c2:
                return 0
            
            # try all horizontal cuts
            ans = float('inf')
            for row in range(r1,r2):
                top_part = dp(r1,c1,row, c2)
                down_part = dp(row+1,c1, r2,c2 )
                ans = min(ans, top_part + down_part + horizontalCut[row])

            # try all vertical cuts
            for col in range(c1, c2):
                left_part = dp(r1, c1, r2, col)
                right_part = dp(r1, col+1, r2, c2 )
                ans = min(ans, left_part + right_part + verticalCut[col])
            
            memo[(r1,c1,r2,c2)] = ans
            return memo[(r1,c1,r2,c2)]
        
        return dp(0, 0, m - 1, n - 1)
        
