# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l = 0
        temp = head
        while temp is not None:
            l+=1
            temp = temp.next
        
        dummy = ListNode(0,next = head)
        l = l - n
        first = dummy
        while l:
            l-=1
            first = first.next
        first.next = first.next.next
        return dummy.next




