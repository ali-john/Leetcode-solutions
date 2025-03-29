# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):

            if not node: return True, 0

            leftRes = solve(node.left)
            rightRes = solve(node.right)

            isLeftUniValue = leftRes[0]
            isRightUniValue = rightRes[0]
            
            count = leftRes[1] + rightRes[1]
            if isLeftUniValue and isRightUniValue:
                if node.left and node.left.val != node.val:
                    return False, count
                
                if node.right and node.right.val != node.val:
                    return False, count
                return True, count + 1
            
            return False, count
        
        return solve(root)[1]
        
