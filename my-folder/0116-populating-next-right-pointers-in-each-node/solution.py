"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return None
        q = [(root,0)]
        while q:
            node,level = q.pop(0)
            if q and q[0][1]==level:
                node.next = q[0][0]
            else: node.next = None

            if node.left and node.right:
                q.append((node.left,level+1))
                q.append((node.right,level+1))
        return root
        
