class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def find_row():
            start_row = 0
            end_row = len(matrix)-1
            while start_row<=end_row:
                mid = (start_row+end_row)//2
                num = matrix[mid][0]

                if num==target:
                    return True
                
                elif num>target:
                    end_row = row = mid-1
                elif num<target:
                    col_left = 1
                    col_right = len(matrix[mid])-1
                    start_row =  mid+1
                    while col_left<=col_right:
                        mid_n = (col_left+col_right)//2
                        if matrix[mid][mid_n] == target:
                            return True
                        elif matrix[mid][mid_n]>target:
                            col_right = mid_n-1
                        elif matrix[mid][mid_n]<target:
                            col_left = mid_n+1
                        

            return False
        
        return find_row()
        
        
            

            
        
