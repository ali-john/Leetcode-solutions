# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def counter(self,root,l):
        if root is None:
            return 
        l[0]+=1
        self.counter(root.left,l)
        self.counter(root.right,l)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = root.left if root is not None else None
        r = root.right if root is not None else None
        left_levels = 1
        right_levels = 1
        while(l):
            l = l.left
            left_levels+=1
        while (r):
            r = r.right
            right_levels+=1
        if left_levels==right_levels:
            return 2**left_levels -1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


        

        
