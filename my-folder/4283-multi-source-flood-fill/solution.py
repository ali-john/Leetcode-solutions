class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0]*m for _ in range(n)]
        sources.sort(key=lambda x:-x[2])

        q = deque()
        for row,col, color in sources:
            grid[row][col] = color
            q.append([row,col])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r,c = q.popleft()
            color = grid[r][c]

            for direction in directions:
                new_x = r + direction[0]
                new_y = c + direction[1]
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = color
                    q.append([new_x,new_y])
        return grid
        

