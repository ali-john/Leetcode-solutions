class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        negatives = 0
        min_num = float('inf')
        curr_sum = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negatives+=1
                min_num = min(min_num, abs(matrix[i][j]))
                curr_sum+=abs(matrix[i][j])
        if negatives%2 == 0:
            return curr_sum
        else:
            return curr_sum - (2*min_num)
            
