class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1]*n
        
        def find(value):
            if root[value]==value:
                return value
            root[value] = find(root[value])
            return root[value]
        
        def union(u,v):
            u_parent = find(u)
            v_parent = find(v)
            if u_parent!=v_parent:
                if rank[u_parent] > rank[v_parent]:
                    root[v_parent] = u_parent
                elif rank[v_parent] > rank[u_parent]:
                    root[u_parent] = v_parent
                else:
                    root[u_parent] = v_parent
                    rank[v_parent]+=1
        def is_connected(u,v):
            return find(u)==find(v)
        
        for i in range(n):
            edges = isConnected[i]
            for j in range(n):
                if edges[j]==1:
                    next_edges = j+1
                    while next_edges<n:
                        if edges[next_edges]==1:
                            union(j,next_edges)
                        next_edges+=1
        total_provinces = 0
        for i in range(n):
            if find(i)==i:
                total_provinces+=1
        return total_provinces
                    
        
        
        
