# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        q = []
        q.append(root)
        level = 0
        while q:
            level+=1
            levelSize = len(q)

            for _ in range(levelSize):
                root = q.pop(0)
                if root.left is None and root.right is None:
                    return level
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
        

        
