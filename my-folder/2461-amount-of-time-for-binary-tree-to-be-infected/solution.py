# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = {}
        q = [root]
        while q:
            node = q.pop(0)
            if node.val not in graph:
                graph[node.val] = []
            if node.left is not None:
                graph[node.val].append(node.left.val)
                if node.left.val not in graph: graph[node.left.val] = []
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right is not None:
                graph[node.val].append(node.right.val)
                if node.right.val not in graph: graph[node.right.val] = []
                graph[node.right.val].append(node.val)
                q.append(node.right)
        ans = 0
        q = [(start,0)]
        visited = set()
        while q:
            node, lvl = q.pop(0)
            visited.add(node)
            ans = max(ans,lvl)
            for nei in graph[node]:
                if nei not in visited:
                    q.append((nei,lvl+1))
        return ans



            

