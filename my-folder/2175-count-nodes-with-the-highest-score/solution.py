class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        for node,parent in enumerate(parents):
            tree[parent].append(node)
        n = len(parents)
        count = collections.Counter()
        
        def dfs(node):
            p,s = 1, 0 
            
            for child in tree[node]:
                res = dfs(child)
                p*=res
                s+=res
            p = p * max(1,n-1-s) # multiply current product with rest of tree that is not rooted at current node
            count[p]+=1
            return s+1
        dfs(0)
        return count[max(count.keys())]



        

