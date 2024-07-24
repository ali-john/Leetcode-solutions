# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node,paths,targetSum):
            if not node:
                return 
            paths.append(node.val)
            if node.val == targetSum and node.left == None and node.right == None:
                output.append(paths[:])
            
            dfs(node.left,paths,targetSum-node.val)
            dfs(node.right,paths,targetSum-node.val)
            paths.pop()

        output = []
        dfs(root,[],targetSum)
        return output
        


        
