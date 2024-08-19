# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = defaultdict(int)
        def sub_sum(root):
            if not root:
                return 0
            
            current_sum = root.val + sub_sum(root.left)+ sub_sum(root.right)
            sums[current_sum]+=1
            return current_sum
        
        sub_sum(root)
        max_value = max(sums.values())
        max_keys = [key for key,value in sums.items() if value==max_value]
        return max_keys


            
        
