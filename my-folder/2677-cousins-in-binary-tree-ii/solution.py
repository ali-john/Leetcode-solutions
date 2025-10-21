# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = []
        q = deque([root])
        # get all levels sum
        while q:
            lvl_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                lvl_sum+=node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            levels.append(lvl_sum)
        # update values
        q = deque([(root, root.val)])
        level = 0
        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                node.val = levels[level] - val
                
                child_sum = 0
                if node.left is not None:
                    child_sum+=node.left.val
                if node.right is not None:
                    child_sum+= node.right.val
                
                if node.left is not None:
                    q.append((node.left, child_sum))
                if node.right is not None:
                    q.append((node.right, child_sum))
            level+=1
        return root




