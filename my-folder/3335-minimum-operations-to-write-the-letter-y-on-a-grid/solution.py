class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y_cells = set()
        # generate top left diagonal
        for i in range(n//2):
            y_cells.add((i,i))
        # generate right diagonal
        r = 0
        for c in range(n - 1, n // 2, -1):
            y_cells.add((r,c))
            r+=1
        
        # down cells:
        for r in range(n//2, n):
            y_cells.add((r,n//2))
        
        # count each element:
        y_table = {0:0, 1:0, 2:0}
        outside = {0:0, 1:0, 2:0}

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if (i,j) in y_cells:
                    y_table[val]+=1
                else:
                    outside[val]+=1
        
        # run cases:
        def find_changes(y_label, outside_label):
            y_changes = len(y_cells) - y_table[y_label]
            outside_cells = n**2 - len(y_cells)
            outside_changes = outside_cells - outside[outside_label]
            total = y_changes + outside_changes
            return total

        ans = float('inf')
        # y ->0 , outside 1
        c1 = find_changes(0,1)
        c2 = find_changes(0,2)
        c3 = find_changes(1,0)
        c4 = find_changes(1,2)
        c5 = find_changes(2,0)
        c6 = find_changes(2,1)
        
        return min(c1,c2,c3,c4,c5,c6)





