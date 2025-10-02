class UnionFind:

    def __init__(self,n):
        self.rank = [1]* n
        self.root = [i for i in range(n)]

    def find(self,value):
        if self.root[value] == value:
            return value
        
        self.root[value] = self.find(self.root[value])
        return self.root[value]
    
    def union(self, u, v):
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
        return self.find(u) == self.find(v)
    

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        n = len(properties)
        m = len(properties[0])

        uf = UnionFind(n)
        for i in range(n):
            s1 = set(properties[i])
            for j in range(n):
                if i == j: continue
                s2 = set(properties[j])
                if uf.is_connected(i,j): continue
                else:
                    res = list(s1.intersection(s2))
                    if len(res)>=k:
                        uf.union(i,j)
                    # count = 0
                    # for num in s1:
                    #     if num in s2:
                    #         count+=1
                    
                    # if count >=k:
                    #     uf.union(i,j)
        
        # count connected components:
        # set correct parents
        uf.find(0)

        ans = 0
        for i in range(n):
            if uf.find(i) == i:
                ans+=1
        return ans



        
