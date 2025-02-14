# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            if not root: return True,0

            left = solve(root.left)
            right = solve(root.right)
            isLeftUniValue = left[0]
            isRightUniValue = right[0]

            count = left[1] + right[1]
            if isLeftUniValue and isRightUniValue:
                if root.left and root.val!=root.left.val:
                    return False,count
                if root.right and root.val!=root.right.val:
                    return False,count
                return True,count+1
            
            return False,count
            
            
        return solve(root)[1]

            

          
        





            
