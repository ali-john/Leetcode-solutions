class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        diagonals = defaultdict(list)

        for i in range(rows):
            for j in range(cols):
                diagonals[i-j].append(mat[i][j])
        #print(diagonals)
        new_mat = [[0]*cols for _ in range(rows)]
        for key,val in diagonals.items():
            val.sort()
        for i in range(rows):
            for j in range(cols):
                new_mat[i][j] = diagonals[i-j].pop(0)

        return new_mat
