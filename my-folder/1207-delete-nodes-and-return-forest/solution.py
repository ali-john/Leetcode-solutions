# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        output = []
        to_delete = set(to_delete)
        def solve(root,parent):
            if root is None:
                return 
            left = solve(root.left,root)
            right = solve(root.right,root)

            if root.val in to_delete:
                if left is not None:
                    output.append(left)
                if right is not None:
                    output.append(right)
                if parent is not None:
                    if parent.left==root:
                        parent.left = None
                    else:
                        parent.right = None
            else:
                return root
            
        solve(root,None)
        if root.val not in to_delete:
            output.append(root)
        return output

            
