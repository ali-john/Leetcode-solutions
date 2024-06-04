# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        if root.left is not None and root.right is not None:
            starter_n = root.left
            while starter_n.right is not None:
                starter_n = starter_n.right
            
            temp = root.right
            root.right = root.left
            starter_n.right = temp
            root.left = None
        elif root.left is not None and root.right is None:
            root.right = root.left
            root.left = None

        return root




    


        
