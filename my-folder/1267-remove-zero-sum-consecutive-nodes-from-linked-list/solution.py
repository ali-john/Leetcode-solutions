# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0,head)
        current = front
        prefix = 0
        table = defaultdict()
        while current:
            prefix+=current.val

            if prefix in table:
                prev = table[prefix]
                current = prev.next
                p = prefix + current.val
                while p!=prefix:
                    del table[p]
                    current = current.next
                    p+=current.val
                prev.next = current.next
            else:
                table[prefix] = current
            current = current.next
        return front.next


        
        
        

        
