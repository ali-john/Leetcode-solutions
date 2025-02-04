class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        

        memo = {}
        def dp(left,right,c1,c2):
            #if left<0 or right>=n: return float('inf')
            if (left,right,c1,c2) in memo: return memo[(left,right,c1,c2)]

            if left == right - 1:
                if c1==c2: result = float('inf')
                else: result =  cost[left][c1] + cost[right][c2]

            else:
                if c1==c2: result =  float('inf')
                else:
                    result = float('inf')
                    for color_1 in range(3):
                        for color_2 in range(3):
                            if color_1 == color_2: continue
                            elif color_1 == c1 or color_2==c2:continue
                            else:
                                result = min(result, cost[left][c1] + cost[right][c2] + dp(left+1,right-1,color_1,color_2))
                

            memo[(left,right,c1,c2)] = result
            return result
        out = float('inf')
        for c1 in range(3):
            for c2 in range(3):
                out = min(out, dp(0,n-1,c1,c2) )
        return out
            
        
        
        
            
