# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_a= [0]
        def dfs(root):
            if not root:
                return 
            if root.left is not None:
                next_l = root.left
                if next_l.left is None and next_l.right is None:
                    sum_a[0]+=next_l.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sum_a[0]

