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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        emails_dict = defaultdict(int)

        for i,email in enumerate(accounts):
            for e in email[1:]:
                if e in emails_dict:
                    uf.union(i,emails_dict[e])
                else:
                    emails_dict[e] = i
        leader_to_emails = defaultdict(list)
        for e,i in emails_dict.items():
            leader = uf.find(i)
            leader_to_emails[leader].append(e)
        res = []
        for key,val in leader_to_emails.items():
            name = accounts[key][0]
            res.append([name] + sorted(val))
        return res


























        
