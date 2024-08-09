# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(output,root):
            if not root:
                return None
            
            inorder(output,root.left)
            output.append(root.val)
            inorder(output,root.right)
        output = []
        inorder(output,root)
        return output
        

