# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 1
        q = []
        q.append(root)
        maxSum = float("-inf")
        levelNum = 0
        outputLevel = 0
        while q:
            levelSize = len(q)
            levelSum = 0
            levelNum+=1
            for _ in range(levelSize):
                root = q.pop(0)
                levelSum+=root.val
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            if levelSum>maxSum:
                maxSum = levelSum
                outputLevel = levelNum
        return outputLevel

            
        
