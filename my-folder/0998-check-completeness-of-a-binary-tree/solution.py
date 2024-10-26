# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def check(l)->bool:
            after = False
            null_val = False
            for node in l:
                if null_val:
                    if node:
                        return False
                if node is None:
                    null_val = True
            return True

        def bfs(node)->bool:
            q = [node]
            while q:
                s = len(q)
                current_iter = []
                space_available = False
                for i in range(s):
                    curr = q.pop(0)
                    if curr:
                        current_iter.append(curr.left)
                        current_iter.append(curr.right)
                        if not(curr.left and curr.right):
                            space_available = True
                        q.append(curr.left)
                        q.append(curr.right)
                if not check(current_iter):
                    return False
                if space_available:
                    for node in q:
                        if node:
                            if node.right or node.left:
                                return False
            return True

        return bfs(root)


