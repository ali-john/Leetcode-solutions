class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def is_vshape_or_hitwall(row, column):
            if grid[row][column] == 1:
                if column + 1 < n:
                    if grid[row][column + 1] == -1:
                        return True
                else:
                    return True
            else:
                if column - 1 >= 0:
                    if grid[row][column - 1] == 1:
                        return True
                else:
                    return True
            return False


        def dfs(row, column):
            # V shape cases
            if is_vshape_or_hitwall(row, column):
                return -1
            # last cell redirection
            if row == m - 1:
                if grid[row][column] == 1:
                    return column + 1 if ( column + 1 ) < n else -1
                if grid[row][column] == -1:
                    return column - 1 if (column - 1) >= 0 else -1
            
              
            if grid[row][column] == 1:
                ans = dfs(row+1, column+1)
                if ans != -1:
                    return ans
            else:
                ans = dfs(row+1, column - 1)
                if ans!=-1:
                    return ans
            return -1




        ans = [-1]*n
        for ball in range(0, n):
            out = dfs(0, ball)
            if out!=-1:
                ans[ball] = out
        return ans


