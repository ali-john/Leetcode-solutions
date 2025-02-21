class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        table = defaultdict(list)
        for i in range(m):
            for j in range(n):
                table[i-j].append(mat[i][j])
        for key,_ in table.items():
            table[key].sort(reverse = True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = table[i-j].pop()
        
        return mat
        

