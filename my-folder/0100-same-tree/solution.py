# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,tree,output=[]):
        if tree is None:
            output.append(None)
            return
        else:
            output.append(tree.val)
            self.inOrder(tree.left,output)
            self.inOrder(tree.right,output)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pout = []
        qout = []
        self.inOrder(p,output=pout)
        self.inOrder(q,output = qout)

        if pout == qout:
            return True
        else:
            return False



        
