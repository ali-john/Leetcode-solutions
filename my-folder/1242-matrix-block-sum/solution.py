class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # build prefix sum matrix
        matrix = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                matrix[i][j] = mat[i-1][j-1] + matrix[i-1][j]+ matrix[i][j-1] - matrix[i-1][j-1]
        
        answer = [[0]*n for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                i1 = max(i - k-1, 0)
                j1 = max(j - k-1, 0)
                i2 = min(i + k, m)
                j2 = min(j + k, n)
                answer[i-1][j-1] = matrix[i2][j2] - matrix[i1][j2]-matrix[i2][j1] + matrix[i1][j1]
        

        return answer
