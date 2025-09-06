class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_ops = 0
        for i in range(m):
            row = grid[i]
            start = 0
            end = n - 1
            while start <= end:
                if row[start]!=row[end]:
                    row_ops+=1
                start+=1
                end-=1
        
        col_ops = 0

        for i in range(n):
            col = []
            for j in range(m):
                col.append(grid[j][i])
            
            start = 0
            end = len(col) - 1
            while start <= end:
                if col[start]!=col[end]:
                    col_ops+=1
                start+=1
                end-=1
        return min(row_ops, col_ops)

                
