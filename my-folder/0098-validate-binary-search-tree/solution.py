# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,output):
        if not root:
            return
        self.check(root.left,output)
        output.append(root.val)
        self.check(root.right,output)

            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = [True]
        self.check(root,output)
        vals = output[1:]
        for i in range(len(vals)-1):
            if vals[i+1]<=vals[i]:
                output[0] = False
        return output[0]
        
