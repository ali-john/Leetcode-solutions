class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        GUARD, WALL, CLEAR = 3, 2, -1
        grid = [[CLEAR]*n for _ in range(m)]
        for gi,gy in guards: grid[gi][gy] = GUARD
        for wi,wy in walls: grid[wi][wy] = WALL
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for gx,gy in guards:
            for dire in directions:
                new_x , new_y = gx + dire[0], gy + dire[1]
                while new_x >=0 and new_x < m and new_y >=0 and new_y < n and grid[new_x][new_y]!= GUARD and grid[new_x][new_y]!=WALL:
                    grid[new_x][new_y] = 0
                    new_x , new_y = new_x + dire[0], new_y + dire[1]
        
        return sum( [1 for j in range(n) for i in range(m) if grid[i][j] == CLEAR ])


            
            
        

