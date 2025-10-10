# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        lengths = []
        
        def getLengths(root):
            if not root: return (0, True)
            left_count, left_dec = getLengths(root.left)
            right_count, right_dec = getLengths(root.right)
            
            isPerfect = False
            if ( left_count == right_count) and ( left_dec and right_dec):
                lengths.append(left_count + right_count + 1)
                isPerfect = True
            
            return (left_count + right_count + 1, isPerfect)
        
        getLengths(root)
        lengths.sort(reverse = True)
        return lengths[k-1] if len(lengths)>= k else -1 


