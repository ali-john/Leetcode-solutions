# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, goLeft, steps):
            if node is None: return 0
            nonlocal ans
            ans = max(ans, steps)
            if goLeft:
                dfs(node.left, False, steps+1)
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, steps+1)
                dfs(node.left, False, 1)
        dfs(root, True, 0)
        return ans




