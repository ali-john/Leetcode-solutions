# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        output = []
        to_delete = set(to_delete)
        def dfs(root,parent):
            if not root:
                return None
            
            left = dfs(root.left,root)
            right = dfs(root.right,root)
            if root.val in to_delete:
                if left is not None:
                    output.append(left)
                if right is not None:
                    output.append(right)
                if parent is not None:
                    if parent.left==root:
                        parent.left=None
                    else:
                        parent.right= None
                
            else:
                return root
        r = dfs(root,None)
        if r is not None:
            output.append(r)
        return output



