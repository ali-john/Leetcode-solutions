class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = deepcopy(matrix)
        r,c = len(matrix), len(matrix[0])

        def find_max(i,j):
            val = 0
            for k in range(r):
                val = max(val,matrix[k][j])
            return val
                
        for row in range(r):
            for col in range(c):
                if matrix[row][col]==-1:
                    new_matrix[row][col]=find_max(row,col)
        return new_matrix
                    
