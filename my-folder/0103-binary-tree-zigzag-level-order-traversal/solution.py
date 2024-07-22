# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = []
        q.append(root)
        output = []
        leftToRight = True
        while len(q)>0:
            size = len(q)
            level = []
            for _ in range(size):
                root = q.pop(0)
                if leftToRight:
                    level.append(root.val)
                else:
                    level.insert(0,root.val)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            output.append(level)
            leftToRight = not leftToRight
        return output
                    
                    
                

