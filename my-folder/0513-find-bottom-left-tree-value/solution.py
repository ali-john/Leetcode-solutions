# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            q = []
            q.append(root)
            last = root.val
            while q:
                last = q[0].val
                root = q.pop(0)
                if root.right is not None:
                    q.append(root.right)
                if root.left is not None:
                    q.append(root.left)
            return last
        return bfs(root)

        
