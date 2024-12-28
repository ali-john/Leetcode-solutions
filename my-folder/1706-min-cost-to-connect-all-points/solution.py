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

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i+1,n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight,i,j))
        edges.sort()

        mst = 0
        edges_used = 0
        uf = UnionFind(n)

        for weight,p1,p2 in edges:
            uf.find(p1)
            uf.find(p2)
            if not uf.is_connected(p1,p2):
                mst+=weight
                uf.union(p1,p2)
                edges_used+=1
                if edges_used==n-1: break
        return mst



        
        
