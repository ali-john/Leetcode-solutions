# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def dfs(root,val):
            if root is None:
                return None
            
            if val==root.val:
                return root
            elif val>root.val:
                return dfs(root.right,val)
            else:
                return dfs(root.left,val)

        out = dfs(root,val)
        if out is None:
            return None
        else:
            return out
