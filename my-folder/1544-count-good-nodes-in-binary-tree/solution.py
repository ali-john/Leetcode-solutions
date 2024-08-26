# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = [0]
        def dfs(root,val):
            if not root:
                return
            
            val = max(val,root.val)
            if root.val>=val:
                cnt[0]+=1
            dfs(root.left,val)
            dfs(root.right,val)
        dfs(root,float("-inf"))
        return cnt[0]
            

