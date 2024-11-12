class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        rows,cols = len(grid),len(grid[0])
        # just iterate each row and use BS to find negative elements
        for i in range(rows):
            col = grid[i]
            left = 0
            right = cols
            while left<right:
                mid = (left+right)//2
                if col[mid]<0:
                    right = mid        
                else:
                    left = mid+1
                    
            ans+=(cols - left)
                
        return ans
