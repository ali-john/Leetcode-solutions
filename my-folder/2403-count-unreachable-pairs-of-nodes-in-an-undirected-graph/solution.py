class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, node):
        if self.root[node] == node:
            return self.root[node]
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent != v_parent:
            if self.rank[u_parent] > self.rank[v_parent]:
                self.root[v_parent] = u_parent
            elif self.rank[v_parent] > self.rank[u_parent]:
                self.root[u_parent] = v_parent
            else:
                self.root[u_parent] = v_parent
                self.rank[v_parent]+=1

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edg1, edg2 in edges:
            uf.union(edg1, edg2)

        componentSizes = defaultdict(int)
        for i in range(n):
            componentSizes[uf.find(i)]+=1
        #print(componentSizes)
        ans = 0
        for _, component_size in componentSizes.items():
            rem_nodes = n - component_size
            ans+= (component_size*rem_nodes) / 2
        return int(ans)


        
