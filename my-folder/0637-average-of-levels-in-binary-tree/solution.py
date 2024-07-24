import numpy as np
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        q = []
        q.append(root)

        while q:
            levelSize = len(q)
            levelSum = 0
            for _ in range(levelSize):
                root = q.pop(0)
                levelSum+=root.val
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            output.append(levelSum/levelSize)
        return output
                
                



            
            
            
            




        

                
            
            
            
            




        
