# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def backtrack(start,end):
            result = []
            if start>end:
                result.append(None)
                return result
            
            for i in range(start,end+1,1):
                left_trees = backtrack(start,i-1)
                right_trees = backtrack(i+1,end)
                for j in range(len(left_trees)):
                    for k in range(len(right_trees)):
                        root = TreeNode(i,left_trees[j],right_trees[k])
                        result.append(root)
            return result
        return backtrack(1,n)




