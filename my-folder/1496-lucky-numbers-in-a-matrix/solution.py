class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        for i in range(n):
            min_element = (float('inf'),0) #number , index
            for j in range(m):
                if matrix[i][j]<min_element[0]:
                    min_element = (matrix[i][j],j)
            
            # check if it is max in column or not
            is_max = True
            for row in range(n):
                if min_element[0] < matrix[row][min_element[1]]:
                    is_max = False
            if is_max:
                ans.append(min_element[0])
        return ans


