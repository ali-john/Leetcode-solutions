class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m  = len(grid) # rows
        n = len(grid[0]) # cols
        
        row_operation = 0
        for i in range(m):
            row = grid[i]
            startPtr = 0
            endPtr = len(row)-1
            while startPtr<=endPtr:
                if row[startPtr]!=row[endPtr]:
                    row_operation+=1
                startPtr+=1
                endPtr-=1
        
        col_operation = 0
        
        for i in range(n):
            col = []
            for j in range(m):
                col.append(grid[j][i])
            
            startPtr = 0
            endPtr = len(col)-1
            while startPtr<=endPtr:
                if col[startPtr]!=col[endPtr]:
                    col_operation+=1
                startPtr+=1
                endPtr-=1
            
        return min(row_operation,col_operation)


