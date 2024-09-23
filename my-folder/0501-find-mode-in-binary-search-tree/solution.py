# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        table = defaultdict(int)

        def recur(root):
            if not root:
                return
            table[root.val]+=1
            recur(root.left)
            recur(root.right)
        
        recur(root)
        max_vals = []
        vals = max(table.values())
        for key,val in table.items():
            if val==vals:
                max_vals.append(key)
        return max_vals

        
