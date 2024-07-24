# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node,paths):
            if not node:
                return 
            paths.append(node.val)
            if node.left == None and node.right == None:
                formatted = "->".join(map(str,paths))
                output.append(formatted)
            
            dfs(node.left,paths)
            dfs(node.right,paths)
            paths.pop()
        
        output = []
        dfs(root,[])
        return output


        
