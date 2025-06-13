class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        #ans = [ [0 for _ in range(m-k+1)] for _ in range(n-k+1)]
        ans = []


        for i in range(m - k + 1):
            temp = []
            for j in range(n -k + 1):
                sub_matrix = []
                s = set()
                for t in range(i,i+k):
                    for x in range(j,j+k):
                        if grid[t][x] not in s:
                            sub_matrix.append(grid[t][x])
                            s.add(grid[t][x])
                    
                #print(sub_matrix)
                sub_matrix.sort()
                min_diff = float('inf')
                if len(sub_matrix)>1:
                    for y in range(1, len(sub_matrix)):
                        min_diff = min(min_diff, abs(sub_matrix[y] - sub_matrix[y-1]))
                else:
                    min_diff = 0
                #print(min_diff)
                temp.append(min_diff)
            ans.append(temp)
        return ans
                    
