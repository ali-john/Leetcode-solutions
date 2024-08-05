class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)

    def adjacentSum(self, value: int) -> int:
        row = 0
        col = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j]==value:
                    row = i
                    col = j
                    break
        output = 0
        # top sum:
        if row-1>=0 and row-1<self.n:
            output+=self.grid[row-1][col]
        # bottom sum:
        if row+1<self.n:
            output+=self.grid[row+1][col]
        # left sum:
        if col+1<self.n:
            output+=self.grid[row][col+1]
        # right sum:
        if col-1>=0 and col-1<self.n:
            output+=self.grid[row][col-1]
        return output

    def diagonalSum(self, value: int) -> int:
        row = 0
        col = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j]==value:
                    row = i
                    col = j
                    break
        output = 0
        # top left:
        if row-1>=0 and col-1>=0:
            output+=self.grid[row-1][col-1]
        # top - right
        if row-1>=0 and col+1<self.n:
            output+=self.grid[row-1][col+1]
        # bottom-left:
        if row+1<self.n and col-1>=0:
            output+=self.grid[row+1][col-1]
        # bottom-right:
        if row+1<self.n and col+1<self.n:
            output+=self.grid[row+1][col+1]
        return output
        
        
# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
