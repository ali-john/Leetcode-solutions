class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        output = []
        rows = []
        cols = []
        row_inc = False
        col_inc = True
        row_dec = False
        col_dec = False
        row = 0
        col = 0

        while len(output)!= m*n:
            if col_inc:
                if row not in rows:
                    while col<n and col not in cols:
                        output.append(matrix[row][col])
                        col+=1
                rows.append(row)
                col_inc = False
                row_inc = True
            elif row_inc:
                col = col-1
                row+=1
                if col not in cols:
                    while row<m and row not in rows:
                        output.append(matrix[row][col])
                        row+=1   
                cols.append(col)
                row_inc = False
                col_dec = True
            elif col_dec:
                row-=1
                col-=1
                if row not in rows:
                    while col>=0 and col not in cols:
                        output.append(matrix[row][col])
                        col-=1 
                rows.append(row)
                col_dec = False
                row_dec = True
            elif row_dec:
                col+=1
                row-=1
                if col not in cols:
                    while row>=0 and row not in rows:
                        output.append(matrix[row][col])
                        row-=1
                cols.append(col)
                col+=1
                row+=1
                row_dec = False
                col_inc = True
        return output
                




                    


                




        
