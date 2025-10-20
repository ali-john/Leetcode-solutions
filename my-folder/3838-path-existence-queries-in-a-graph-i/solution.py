class UnionFind:
    def __init__(self, n:int):
        self.rank = [1]*n
        self.root = [i for i in range(n)]
    def find(self,value):
        if self.root[value] == value:
            return value
        self.root[value] = self.find(self.root[value])
        return self.root[value]
    
    def union(self, u,v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent != v_parent:
            if self.rank[u_parent] > self.rank[v_parent]:
                self.root[v_parent] = u_parent
            elif self.rank[u_parent] < self.rank[v_parent]:
                self.root[u_parent] =  v_parent
            else:
                self.root[u_parent] = v_parent
                self.rank[v_parent]+=1
    def is_connected(self,u,v):
        return self.find(u) == self.find(v)


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        uf = UnionFind(n)

        for i in range(1,n):
            if abs ( nums[i] - nums[i-1] ) <= maxDiff:
                uf.union(i,i-1)

        ans = []
        for start,end in queries:
            if uf.find(start) == uf.find(end): ans.append(True)
            else: ans.append(False)
        return ans

        
