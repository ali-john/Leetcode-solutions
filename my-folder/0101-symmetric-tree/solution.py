# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node,output=[]):
        if node is None:
            output.append(None)
            return
        else:
            output.append(node.val)
            self.preorder(node.left,output)
            self.preorder(node.right,output)

    def anyorder(self,node,left=[]):
        if node is None:
            left.append(None)
            return
        else:
            left.append(node.val)
            self.anyorder(node.right,left)
            self.anyorder(node.left,left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is not None:
            return False
        elif root.left is not None and root.right is None:
            return False
        elif root.left is None and root.right is None:
            return True
        else:
            left = []
            right = []
            rightN = root.right
            leftN = root.left
            self.preorder(rightN,output = right)
            self.anyorder(leftN,left = left)
            if left==right:
                return True
                
            else:
                return False
        
        
