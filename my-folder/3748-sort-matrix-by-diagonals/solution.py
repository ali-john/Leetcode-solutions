class Solution:
    def sortMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)

        table = defaultdict(list)
        for i in range(n):
            for j in range(n):
                table[i-j].append(mat[i][j])
        ans = [[0]*n for _ in range(n)]
        for key,val in table.items():
            if key < 0:
                val.sort()
            else:
                val.sort(reverse = True)
        
        for i in range(n):
            for j in range(n):
                ans[i][j] = (table[i-j].pop(0))
        return ans




















        # n = len(mat)
        # table = defaultdict(list)

        # for i in range(n):
        #     for j in range(n):
        #         table[i-j].append(mat[i][j])
        
        # for key,_ in table.items():
        #     if key<0:
        #         table[key].sort()
        #     else:
        #         table[key].sort(reverse = True)
        # new_mat = [ [0]*n for _ in range(n)]
        # #print(table)
        # for i in range(n):
        #     for j in range(n):
        #         new_mat[i][j] = table[i-j].pop(0)
        # return new_mat

