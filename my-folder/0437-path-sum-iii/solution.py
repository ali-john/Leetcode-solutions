# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,paths):
            if not node:
                return 0
            
            paths.append(node.val)
            path_sum = 0
            total_paths = 0
            for i in range(len(paths)-1,-1,-1):
                path_sum+=paths[i]

                if path_sum==targetSum:
                    total_paths+=1
            
            total_paths += dfs(node.left,paths)
            total_paths += dfs(node.right,paths)
            paths.pop()
            return total_paths
        
        return dfs(root,[])
        




        
