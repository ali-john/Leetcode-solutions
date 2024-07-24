# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        q = []
        q.append(root)

        while q:
            max_depth+=1
            levelSize = len(q)
            for _ in range(levelSize):
                root = q.pop(0)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
        return max_depth
