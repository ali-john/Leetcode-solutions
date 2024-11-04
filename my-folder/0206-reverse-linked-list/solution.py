# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        nextPtr = head
        
        while head is not None:
            nextPtr = head.next
            head.next = prev
            prev = head
            head = nextPtr
        return prev
            
            


