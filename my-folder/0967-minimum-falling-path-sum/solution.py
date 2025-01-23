class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        memo = {}
        def dp(i,j):
            if i<0 or i>=n or j<0 or j>=n:return float('inf')
            if i==n-1: return matrix[i][j]
            if (i,j) in memo: return memo[(i,j)]
            down = matrix[i][j] + dp(i+1,j)
            left = matrix[i][j] + dp(i+1,j-1)
            right = matrix[i][j] + dp(i+1,j+1)

            memo[(i,j)] = min(down,left,right)
            return memo[(i,j)]
        return min([dp(0,i) for i in range(n)])
