# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getSum(self,root,target,upto,dec):
        if root is None:
            return

        root.val = root.val + upto
        val = root.val
        if root.left is None and root.right is None and val==target:
            dec.append(1)
        self.getSum(root.left,target,val,dec)
        self.getSum(root.right,target,val,dec)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        dec = []
        self.getSum(root,targetSum,0,dec)
        if len(dec)>0:
            return True
        else:
            return False
        
        
    


        
