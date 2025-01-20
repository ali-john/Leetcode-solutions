class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        matrix_to_index = defaultdict(list)
        for i in range(n):
            for j in range(m):
                matrix_to_index[mat[i][j]].append(i)
                matrix_to_index[mat[i][j]].append(j)
        rows_table = defaultdict(int)
        cols_table = defaultdict(int)

        #print(matrix_to_index)
        for i in range(n):
            rows_table[i] = 0
        
        for j in range(m):
            cols_table[j] = 0
        
        for i in range(len(arr)):
            val = arr[i]
            #print(f'i = {i}, val = {val}')
            row,col = matrix_to_index[val][0], matrix_to_index[val][1]
            rows_table[row]+=1
            cols_table[col]+=1
            if rows_table[row] == m or cols_table[col] == n:
                return i
        return -1
