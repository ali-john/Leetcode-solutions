class UnionFind:
    def __init__(self,n):
        self.count = n
        self.rank = [1]*n
        self.root = [i for i in range(n)]

    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent != v_parent: # if they are different
            if self.rank[u_parent] > self.rank[v_parent]:
                self.root[v_parent] = u_parent
            elif self.rank[v_parent] > self.rank[u_parent]:
                self.root[u_parent] = v_parent
            else:
                self.root[u_parent] = v_parent
                self.rank[v_parent]+=1
            self.count-=1
    def is_connected(self,u,v):
        return self.find(u) == self.find(v)

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs,key = lambda x: x[0])
        uf = UnionFind(n)
        i = 0
        components = 0
        while i<len(logs):
            time,u,v = logs[i]
            uf.union(u,v)
            if uf.count==1: return time
            i+=1
            
        return -1
        
