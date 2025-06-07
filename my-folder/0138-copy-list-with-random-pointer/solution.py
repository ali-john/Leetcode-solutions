"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        temp = dummy

        start = head

        i = 0
        node_to_index_old = defaultdict()
        index_to_node_old = defaultdict()
        node_to_index_new = defaultdict()
        index_to_node_new = defaultdict()

        while start is not None:
            newNode = Node(start.val)
            temp.next = newNode
            temp = newNode
            
            node_to_index_old[start] = i
            node_to_index_new[newNode] = i

            index_to_node_old[i] = start
            index_to_node_new[i] = newNode

            start = start.next if start else None
            i+=1
        
        temp = dummy.next
        start = head

        while start is not None:
            if start.random is None:
                temp.random = None
            else:
                pointsTo = index_to_node_new[ node_to_index_old[start.random] ]
                temp.random = pointsTo
            
            start = start.next if start else None
            temp = temp.next if temp else None
        
        return dummy.next
                
        

