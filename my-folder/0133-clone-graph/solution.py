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
        
        graph = defaultdict(list)
        new_graph = defaultdict(list)
        
        def dfs(curr):
            if not curr:
                return curr
            if curr in new_graph:
                return new_graph[curr]
            
            new_node = Node(curr.val,[])
            new_graph[curr] = new_node

            if curr.neighbors:
                new_node.neighbors = [dfs(n) for n in curr.neighbors]
            
            return new_node
        
        return dfs(node)




            




            
            
                    

