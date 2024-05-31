# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self,node):
        if node is None:
            return 
        else:
            self.invert(node.right)
            self.invert(node.left)
            temp = node.left
            node.left = node.right
            node.right = temp


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

        





        
