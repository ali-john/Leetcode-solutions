# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        lengths = []
        def find_lengths(node):
            if not node:
                return (0, True)
            left_len, left_dec = find_lengths(node.left)
            right_len, right_dec = find_lengths(node.right)
            isPerfect = False
            if (left_len == right_len and (left_dec and right_dec)):
                lengths.append(left_len + right_len + 1)
                isPerfect = True
            return (left_len + right_len + 1, isPerfect)
        find_lengths(root)
        lengths.sort(reverse = True)
        return lengths[k-1] if len(lengths) >= k else -1
        

