# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def returnSum(self,root,val=0):
        if root is None:
            return 
        root.val = (val*10)+root.val
        val = root.val
        if not root.left and not root.right:
            return val
        left = self.returnSum(root.left,val)
        right = self.returnSum(root.right,val)
        if left and right:
            return left+right
        elif left:
            return left
        else:
            return right
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return (self.returnSum(root))
        

        
