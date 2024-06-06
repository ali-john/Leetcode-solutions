# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        q = []
        q.append(root)

        while(len(q)>0):
            size = len(q)
            levels = []
            for i in range(size):
                root = q.pop(0)
                levels.append(root.val)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            output.append(levels)
        
        return output



        

        
        
