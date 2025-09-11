class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid) # rows
        n = len(grid[0]) # cols

        rows_table = defaultdict(int)
        cols_table = defaultdict(int)
        
        row_total = 0
        col_total = 0
        for i in range(m):
            # iterate every column
            row_sum = 0
            for j in range(n):
                 row_sum+=grid[i][j]
            rows_table[i] = row_sum
            row_total+=row_sum
        
        for j in range(n):
            # iterate every row
            col_sum = 0
            for i in range(m):
                col_sum+=grid[i][j]
            cols_table[j] = col_sum
            col_total+=col_sum
        
        # check if possible to cut row wise:
        running_sum = 0
        for i in range(m):
            running_sum +=rows_table[i]
            remaining_sum = row_total - running_sum
            if running_sum == remaining_sum: return True
        
        # check column wise cut possibility:
        running_sum = 0
        for j in range(n):
            running_sum += cols_table[j]
            remaining_sum = row_total - running_sum
            if running_sum == remaining_sum: return True
        
        return False



