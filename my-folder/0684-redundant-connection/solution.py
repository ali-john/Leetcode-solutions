class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.root = [i for i in range(n)]

    def find(self, value):
        if self.root[value] == value:
            return value
        self.root[value] = self.find(self.root[value])
        return self.root[value]

    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent==v_parent: return False
        if u_parent != v_parent:
            if self.rank[u_parent] > self.rank[v_parent]:
                self.root[v_parent] = u_parent
            elif self.rank[v_parent] > self.rank[u_parent]:
                self.root[u_parent] = v_parent
            else:
                self.root[u_parent] = v_parent
                self.rank[v_parent] += 1
        return True

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        for edge in edges:
            if not uf.union(*edge):
                return edge
                
 
        # previous solution
        # graph = defaultdict(list)
        # n = len(edges)

        # last_edge = -1
        # for i in range(n):
        #     uf = UnionFind(n + 1)
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         uf.union(edges[j][0], edges[j][1])
        #     component = 0
        #     uf.find(n - 1)
        #     for k in range(1, len(uf.root)):
        #         # print(f'k: {k}')
        #         if uf.root[k] == k:
        #             component += 1
        #     # print(f'root:  {uf.root}')
        #     if component == 1:
        #         last_edge = i
        # return edges[last_edge]

