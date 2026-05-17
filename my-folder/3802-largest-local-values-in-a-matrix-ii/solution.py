class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        positions = defaultdict(list)
        for i in range(n):
            for j in range(m):
                positions[matrix[i][j]].append((i,j))
        ans = 0
        for i in range(n):
            for j in range(m):
                x = matrix[i][j]
                if x == 0:
                    continue
                is_local = True
                for bigger in range(x+1, 201):
                    for dx,dy in positions[bigger]:
                        new_i = abs(i - dx)
                        new_j = abs(j - dy)

                        if new_i <= x and new_j <= x:
                            if new_i == x and new_j == x: continue
                            is_local = False
                    if not is_local:
                        break
                if is_local:
                    ans+=1
        return ans

