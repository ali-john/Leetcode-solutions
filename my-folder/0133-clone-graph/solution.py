"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visited = set()
    
        nodes_created = {}
        def bfs(node):
            q = []
            q.append(node)
            
            while q:
                n = q.pop(0)
                nei = n.neighbors
                val = n.val
                keys = nodes_created.keys()
                visited.add(val)
                if val not in keys:
                    new_node = Node(val = val)
                    nodes_created[val] = new_node
                    for i in nei:
                        if i.val not in keys:
                            nn_nei  = Node(val = i.val)
                            nodes_created[i.val] = nn_nei
                            new_node.neighbors.append(nn_nei)
                            q.append(i)
                        else:
                            nn_nei = nodes_created.get(i.val)
                            new_node.neighbors.append(nn_nei)
                            qvals = [x.val for x in q]
                            if not(i.val in visited or i.val in qvals):
                                q.append(i)
                else:
                    new_node = nodes_created.get(val)
                    for i in nei:
                        if i.val not in keys:
                            nn_nei  = Node(val = i.val)
                            nodes_created[i.val] = nn_nei
                            new_node.neighbors.append(nn_nei)
                            q.append(i)
                        else:
                            nn_nei = nodes_created.get(i.val)
                            new_node.neighbors.append(nn_nei)
                            qvals = [x.val for x in q]
                            if not (i.val in visited or i.val in qvals):
                                q.append(i)
                
        
        bfs(node) 
        return nodes_created.get(1)


                

                        








        

        
