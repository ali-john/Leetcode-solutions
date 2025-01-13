class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)

        components = n
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i,j)

        return n-uf.n


class UnionFind:
   def __init__(self,n):
       self.rank = [1]*n
       self.root = [i for i in range(n)]
       self.n = n
  
   def find(self,value):
       if self.root[value]==value:
           return value
       self.root[value] = self.find(self.root[value])
       return self.root[value]
  
   def union(self,u,v):
       u_parent = self.find(u)
       v_parent = self.find(v)
       if u_parent!=v_parent:
           self.n-=1
           if self.rank[u_parent] > self.rank[v_parent]:
               self.root[v_parent] = u_parent
           elif self.rank[v_parent] > self.rank[u_parent]:
               self.root[u_parent] = v_parent
           else:
               self.root[u_parent] = v_parent
               self.rank[v_parent]+=1
  
   def is_connected(self,u,v):
       return self.find(u)==self.find(v)



