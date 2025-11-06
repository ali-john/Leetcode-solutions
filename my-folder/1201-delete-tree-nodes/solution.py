
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        graph = [set() for _ in range(nodes)]
        for cnt, i in enumerate(parent[1:]):
            graph[i].add(cnt+1)
        
        self.ans = nodes # store the total number of nodes
        
        def rec(start):
            if len(graph[start]) == 0: # a leaf does not have any neighbor
                self.ans -= 1 if value[start] == 0 else 0  #only remove a leaf if its value is zero,
                return value[start], 1 if value[start] != 0 else 0 # return leaf value, and number of node that is not removed so far for a leaf it is 0 or 1 depending on leaf's value
            
            s = value[start] # sum for subtree at location start
            d = 1 # number of node below current root, init 1 root itself
            for c in graph[start]:
                sum_temp, n_temp = rec(c)  # for all child calculate sum of thir subtree and number of remaining nodes
                d += n_temp # udate number of subtree
                s += sum_temp # udate sum of  subtree
                
            if s == 0: # if sum == 0 then remove it, all the nodes in this subtree are going so subtract it from self.ans and set d =0 as all nodes in this subtree is already remove
                self.ans -= d
                d = 0
            return s, d
        
        rec(0)
        
        return self.ans
                
        
