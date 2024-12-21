class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 1000000007
        
        @cache
        def solve(i,j,path_sum):
            if i==n-1 and j==m-1 and grid[i][j]^path_sum ==k:
                return 1

            down_path = right_path = 0
            if i+1<n:
                down_path = solve(i+1,j,path_sum^ grid[i][j])
            if j+1<m:
                right_path = solve(i,j+1,path_sum^grid[i][j])

            return (down_path + right_path)%MOD
        
        val = solve(0,0,0)
        return val%MOD
            




