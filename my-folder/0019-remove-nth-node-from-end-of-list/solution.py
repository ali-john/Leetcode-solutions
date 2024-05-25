# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        dummy = dummyNode
        res = dummy

        for _ in range(n):
            head = head.next
        
        while head is not None:
            head = head.next 
            dummy = dummy.next
        
        dummy.next = dummy.next.next
        return res.next


        
    
    


        
