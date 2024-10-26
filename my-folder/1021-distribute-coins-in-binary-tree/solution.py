# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        steps = [0]
        def dfs(node,steps):
            if not node:
                return 0
            
            left_val = dfs(node.left,steps)
            right_val = dfs(node.right,steps)

            steps[0]+=abs(left_val)+abs(right_val)
            return node.val + left_val + right_val - 1

        dfs(root,steps)
        return steps[0]

