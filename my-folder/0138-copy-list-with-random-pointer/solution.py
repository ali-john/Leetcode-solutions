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
        # make a new list
        temp = head
        head2 = Node(0)
        temp2 = head2
        random_pos = {}
        while temp is not None: # Create new nodes 
            val = temp.val
            NewNode = Node(val)
            temp2.next = NewNode
            temp2 = NewNode
            temp = temp.next if temp is not None else None

        temp = head
        present_node=0
        while temp is not None: # Create hashtable for random pointers
            next_node = temp.random
            node_number = 0
            if next_node is None:
                random_pos[present_node] = None
                present_node+=1
                temp = temp.next if temp is not None else None
            else:
                next_data = next_node.val
                temp3 = head
                while not(temp3.val == next_data and temp3==next_node):
                    node_number+=1
                    temp3 = temp3.next
                random_pos[present_node] = node_number
                present_node+=1
                temp = temp.next if temp is not None else None

        head2 = head2.next
        temp = head2
        i = 0
        while temp is not None:
            pos = random_pos[i]
            if pos is None:
                temp.random = None
            else:
                temp1 = head2
                j = 0
                while j!= pos:
                    temp1 = temp1.next
                    j+=1
                temp.random = temp1
            i+=1
            temp = temp.next if temp is not None else None

        return head2




                

                


            


        



        
        
