"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        #stack = []
        output = []
        def post(root):
            if root.children is None:
                return
            
            #stack.append(root.children)
            node_list = root.children
            for node in node_list:
                post(node)
            output.append(root.val)
            
        post(root)
        return output

