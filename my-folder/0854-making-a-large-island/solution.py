
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        table = defaultdict(int)
        zero_count = 0
        one_count = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]==0: zero_count+=1
                else: one_count+=1
        
        if zero_count==(n*n) and one_count==0: return 1
        if zero_count==0: return n*n
        if one_count==0: return 0
        def dfs(i,j,visited,id):
            if i<0 or i>=n or j<0 or j>=n or (i,j) in visited: return

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            grid[i][j] = id
            visited.add((i,j))
            for dx,dy in directions:
                x = i + dx
                y = j + dy
                if x>=0 and x<n and y>=0 and y<n and grid[x][y]==1:
                    dfs(x,y,visited,id)
            return 

        group_num = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    visited = set()
                    dfs(i,j,visited,group_num)
                    table[group_num] = len(visited)
                    group_num+=1
        
        # print(grid)
        # print(table)
        ans = 0
        for i in range(n):
            for j in range(n):
                groups = set()
                if grid[i][j]==0:
                    up,down,left,right = 0,0,0,0
                    if j-1>=0:
                        up = grid[i][j-1]
                        groups.add(up)
                    if j+1<n:
                        down = grid[i][j+1]
                        groups.add(down)
                    if i-1>=0:
                        left = grid[i-1][j]
                        groups.add(left)
                    if i+1<n:
                        right = grid[i+1][j]
                        groups.add(right)
                    sub_ans = 0
                    for g in groups:
                        sub_ans+=table[g]
                    ans = max(ans,sub_ans+1)
                    grid[i][j] = 1
        return ans


        

                































class UnionFind:
   def __init__(self,n):
       self.rank = [1]*n
       self.root = [i for i in range(n)]
  
   def find(self,value):
       if self.root[value]==value:
           return value
       self.root[value] = self.find(self.root[value])
       return self.root[value]
  
   def union(self,u,v):
       u_parent = self.find(u)
       v_parent = self.find(v)
       if u_parent!=v_parent:
           if self.rank[u_parent] > self.rank[v_parent]:
               self.root[v_parent] = u_parent
           elif self.rank[v_parent] > self.rank[u_parent]:
               self.root[u_parent] = v_parent
           else:
               self.root[u_parent] = v_parent
               self.rank[v_parent]+=1
  
   def is_connected(self,u,v):
       return self.find(u)==self.find(v)

