# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            d = self.findDepth(root)
            return d
    
    def findDepth(self,node)->int:
        if node is None:
            return 0
        else:
            leftDepth = self.findDepth(node.left)
            rightDepth = self.findDepth(node.right)

            if leftDepth>rightDepth:
                return leftDepth+1
            else:
                return rightDepth+1
        
        
