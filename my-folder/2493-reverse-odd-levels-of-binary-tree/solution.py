# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(left,right,level):
            if left is None or right is None:
                return 
            
            if level%2==0:
                temp = right.val
                right.val = left.val
                left.val = temp
            
            dfs(left.left,right.right,level+1)
            dfs(left.right,right.left,level+1)
        
        dfs(root.left,root.right,0)
        return root
                












        
        
        
        
        
        # def solve(root):
        #     order = defaultdict(list)
        #     q = [(root,0)]
        #     while q:
        #         node,level = q.pop(0)
        #         order[level].append(node.val)
        #         if node.left is not None and node.right is not None:
        #             q.append((node.left,level+1))
        #             q.append((node.right,level+1))
            
        #     q= [ (root,0)]
        #     while q:
        #         node, level = q.pop(0)
        #         if level%2==0:
        #             if level+1 in order:
        #                 node.left.val = order[level+1][-1]
        #                 node.right.val = order[level+1][-2]
        #                 order[level+1].pop()
        #                 order[level+1].pop()
        #         if node.left is not None and node.right is not None:
        #             q.append((node.left,level+1))
        #             q.append((node.right,level+1))
    
        # solve(root)
        # return root
