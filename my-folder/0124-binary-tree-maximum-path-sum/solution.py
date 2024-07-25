# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_sum = max(dfs(node.left),0)
            right_sum = max(dfs(node.right),0)
            current_sum = left_sum + right_sum + node.val
            max_sum = max(current_sum,max_sum)

            return max(left_sum,right_sum) + node.val
        max_sum = float("-inf")
        dfs(root)
        return max_sum



        
        
