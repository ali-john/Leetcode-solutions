# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root: return []
        output = [root.val]
        q = [(root,0)]

        processed = set()
        processed.add(0)
        while q:
            node,level = q[0]
            
            if level not in processed:
                processed.add(level)
                level_nodes = []
                i = 0
                while q and i< len(q) and q[i][1]==level:
                    level_nodes.append(q[i][0].val)
                    i+=1
                if level_nodes:
                    output.append( sorted(level_nodes)[-1] )
            if node.left is not None: q.append((node.left,level+1))
            if node.right is not None: q.append((node.right,level+1))
            q.pop(0)
        
        return output

