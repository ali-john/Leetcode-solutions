class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
        
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
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        uf = UnionFind(n)
        for u,v in edges:
            u_parent = uf.find(u)
            v_parent = uf.find(v)
            if u_parent==v_parent: return False
            uf.union(u,v)
        components = 0
        for i in range(n):
            if uf.find(i)==i:
                components+=1
                if components>1:
                    return False   
        return True
            
        
        
        
        
