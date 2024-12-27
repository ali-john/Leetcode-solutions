"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        

        if not root: return []

        output = [[root.val]]
        q = [(root,0)]
        level_set = set()
        level_set.add(0)
        while q:
            node,level = q.pop(0)
            if level not in level_set:
                level_set.add(level)
                curr_values = [node.val]
                i = 0
                while q and i< len(q) and q[i][1]==level:
                    curr_values.append(q[i][0].val)
                    i+=1
                output.append(curr_values)
            
            if node.children:
                for child in node.children:
                    q.append((child,level+1))
        return output





