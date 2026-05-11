# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return 0
            mapping[col].append((row, node.val))
            if node.left is not None:
                dfs(node.left, row+1, col -1)
            if node.right is not None:
                dfs(node.right, row+1, col+1)
            return 
        
        dfs(root,0, 0)
        ans = []
        for col in sorted(mapping.keys()):
            values = sorted(mapping[col])
            ans.append([val for row, val in values])
        return ans
            


