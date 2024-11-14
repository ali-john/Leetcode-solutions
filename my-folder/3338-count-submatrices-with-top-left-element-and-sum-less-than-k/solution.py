class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        prefix_sum = [[0]*cols for _ in range(rows)]

        for i in range(cols): # fill first row
            if i==0:
                prefix_sum[0][0]= grid[0][0]
            else:
                prefix_sum[0][i] = grid[0][i] + prefix_sum[0][i-1]
        
        for i in range(1,rows):# fill first column
            prefix_sum[i][0] = grid[i][0] + prefix_sum[i-1][0]

        for row in range(1,rows):
            for col in range(1,cols):
                prefix_sum[row][col] = grid[row][col]+ prefix_sum[row][col-1] + prefix_sum[row-1][col] - prefix_sum[row-1][col-1]
        
        ans = 0
        # now count all sub-matrices
        for row in range(rows):
            for col in range(cols):
                total = prefix_sum[row][col]
                if total<=k:
                    ans+=1
        return ans
