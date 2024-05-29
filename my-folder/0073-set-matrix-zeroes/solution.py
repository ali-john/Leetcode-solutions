class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_set = []
        col = []
        for i in range(len(matrix)): # rows
            for j in range(len(matrix[0])): # cols
                if matrix[i][j]==0:
                    to_set.append((i,j))
        for each in to_set:
            row,col = each
            # set all row to 0:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            # set all column to 0:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        

            



        
