# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            if not root:
                return
            
            left = prune(root.left) 
            right = prune(root.right)
            if left:
                root.left = None
            if right:
                root.right = None
            if root.right==None and root.left==None and root.val == 0:
                return True
            else:
                return False
        
        prune(root)
        if root.left==None and root.right==None and root.val==0:
            return None
        else:
            return root


            
            
       
            

        
