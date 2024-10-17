class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        # add 1 to every row's row1,col1 position and -1 to every row's r,col2+1 position
        for row1,col1,row2,col2 in queries:
            for r in range(row1,row2+1):
                matrix[r][col1]+=1
                if col2+1 <n:
                    matrix[r][col2+1]-=1
        # calculate prefix sum now
        for i in range(n):
            row = matrix[i]
            for j in range(1,n):
                row[j] = row[j]+row[j-1]

        return matrix
