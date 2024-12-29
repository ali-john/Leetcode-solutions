class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        ans = 0

        for i in range(col):
            prev = grid[0][i]
            for j in range(1,row):
                if grid[j][i]>prev:
                    prev = grid[j][i]
                else:
                    next_val = prev + 1
                    diff = abs(grid[j][i] - next_val)
                    ans+=diff
                    grid[j][i]  = next_val
                    prev = next_val
        return ans
