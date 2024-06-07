# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,output):
        if root is None:
            return 
        self.inorder(root.left,output)
        output.append(root.val)
        self.inorder(root.right,output)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        output = []
        self.inorder(root,output)
        diff = 1000000
        for i in range(len(output)-1):
            diff = min(diff,abs(output[i]-output[i+1]))
        return diff

        
