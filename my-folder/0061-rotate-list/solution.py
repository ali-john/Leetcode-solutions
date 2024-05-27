# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        dummy = dummyNode
        
        length = 0
        temp = head
        while temp is not None:
            temp = temp.next if temp is not None else None
            length+=1
        if length == 0 or length ==1:
            return head
        k = k%length # remove cycles
        endptr = head
        prevptr = dummy
        for i in range(k):
            for j in range(length-1):
                endptr = endptr.next
                prevptr = prevptr.next
            head_data = head.val
            endptr.next = head
            head = endptr
            prevptr.next = None
            endptr = head
            dummy.next = head
            prevptr = dummy
        return head
            


        
