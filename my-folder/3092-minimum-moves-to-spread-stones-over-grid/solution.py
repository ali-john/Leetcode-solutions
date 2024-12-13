class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        extras = {}
        zeros = []

        for row in range(3):
            for col in range(3):
                if grid[row][col]==0:  zeros.append((row,col))
                elif grid[row][col]>1: extras[(row,col)] = grid[row][col]
        
        res = float('inf')
        def solve(i,extras,dist):
            nonlocal res
            if i>=len(zeros):
                res = min(res,dist)
                return
            
            for val in extras:
                if extras[val]>1:
                    curr = abs(val[0] - zeros[i][0]) + abs(val[1] - zeros[i][1])
                    extras[val]-=1
                    solve(i+1,extras,dist+curr)
                    extras[val]+=1
        solve(0,extras,0)
        return res
       

