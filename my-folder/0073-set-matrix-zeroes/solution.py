class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        indices = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    indices.add((i,j))
        
        for index in indices:
            row,col = index
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            # set all column to 0:
            for i in range(len(matrix)):
                matrix[i][col] = 0

            
        
