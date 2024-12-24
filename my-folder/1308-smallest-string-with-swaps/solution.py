
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        for u,v in pairs:
            uf.union(u,v)
            if uf.count==1:
                return ''.join(sorted(s))
        
        components = defaultdict(list)

        for i in range(n):
            uf.find(i)
        
        for i,val in enumerate(uf.root):
            components[val].append(i)
        output = ['0']*n

        for key,val in components.items():
            chars = []
            for i in val:
                chars.append(s[i])
            chars = sorted(chars)
            for i,char in zip(val,chars):
                output[i] = char
        return ''.join(output)





class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
        self.count = n
        
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
            self.count-=1
    
    def is_connected(self,u,v):
        return self.find(u)==self.find(v)
        
















        
