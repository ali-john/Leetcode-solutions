# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        leafs = defaultdict(list)

        def collect_leafs(root,path):
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                leafs[root] = path[:]
            path.append('L')
            collect_leafs(root.left,path)
            path.pop()
            path.append('R')
            collect_leafs(root.right,path)
            path.pop()

        
        collect_leafs(root,[])
        leaf_nodes = list(leafs.keys())
        ans = 0

        for i in range(len(leaf_nodes)):
            for j in range(i+1,len(leaf_nodes)):
                l1 = leafs[leaf_nodes[i]]
                l2 = leafs[leaf_nodes[j]]
                # while both are same continue
                ptr = 0
                while ptr< min(len(l1),len(l2)) and l1[ptr]==l2[ptr]:
                    ptr+=1
                
                l1_len = len(leafs[leaf_nodes[i]][ptr:])
                l2_len = len(leafs[leaf_nodes[j]][ptr:])
                if l1_len + l2_len <=distance:
                    ans+=1
        return ans




            
