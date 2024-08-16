# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversal = []
        def order(root):
            if not root:
                return 
            
            order(root.left)
            traversal.append(root.val)
            order(root.right)
        def make(root):
            if not root:
                return
            make(root.left)
            root.val = traversal.pop(0)
            make(root.right)

        order(root)
        traversal = sorted(traversal)
        make(root)
        
        





        
