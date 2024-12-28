class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        time, fresh = 0, 0 

        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1: fresh+=1
                if grid[i][j]==2: q.append((i,j)) # row,col
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh>0:

            for i in range(len(q)):
                node = q.pop(0)
                for dx,dy in directions:
                    new_x = dx + node[0]
                    new_y = dy + node[1]

                    if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y]==1:
                        grid[new_x][new_y] = 2
                        q.append((new_x,new_y))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
                


