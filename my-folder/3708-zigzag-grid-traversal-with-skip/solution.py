class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])

        ans = []
        taken = False
        for i in range(n):
            if i%2==0: # even row->traverse in right
                row = grid[i]
                j = 0
                while j<m:
                    if taken:
                        taken = False
                    else:
                        taken = True
                        ans.append(grid[i][j])
                    j+=1
            else:
                row = grid[i]
                j = m-1
                while j>=0:
                    if taken:
                        taken = False
                    else:
                        taken = True
                        ans.append(grid[i][j])
                    j-=1
        return ans

            
