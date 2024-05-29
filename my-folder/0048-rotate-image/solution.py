class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose the matrix in-place

        for i in range(len(matrix)-1):
            for j in range(i+1, len(matrix)):
                val = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = val
        for row in matrix:
            row.reverse()




        
        
