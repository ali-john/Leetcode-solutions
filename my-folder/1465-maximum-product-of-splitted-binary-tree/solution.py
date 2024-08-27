# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        sums = []
        def get_sum(root)->None:
            if not root:
                return 0
            sub_tree_sum = root.val + get_sum(root.left) + get_sum(root.right)
            sums.append(sub_tree_sum)
            return sub_tree_sum
        
        max_product = 1    
        sum_total = get_sum(root)
        for s in sums:
            product = (s)* (sum_total - s)
            max_product = max(max_product,product)
        return max_product% MOD
        
