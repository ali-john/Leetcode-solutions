class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        directions = [[0,1], [1,0], [0,-1], [-1,0]] # right, down, left, up
        visited = set()


        output = []
        i, j = 0 , 0

        index = 0


        for _ in range(m*n):
            output.append(matrix[i][j])
            visited.add((i,j))
            next_row = i + directions[index][0]
            next_col = j + directions[index][1]

            if (next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or (next_row, next_col) in visited): 
                index = (index+1) % 4

            i+= directions[index][0]
            j+=directions[index][1]
        return output
        
            
                




            



