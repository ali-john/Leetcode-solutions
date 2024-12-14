class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            grid[i].sort(reverse=True)

        ans = 0
        col_start = 0
        for times in range(col):
            max_val = float('-inf')
            for i in range(row):
                max_val = max(max_val,grid[i][col_start])
            ans+=max_val
            col_start+=1
        return ans
                
                

        
