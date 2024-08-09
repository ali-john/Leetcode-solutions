# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        while head is not None:
            temp = head.next if head is not None else None
            while temp is not None and temp.val==head.val:
                temp=temp.next
            head.next = temp
            head = head.next
        return dummy.next
        
