# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        dummy = dummyNode
        res = dummy

        while head is not None:
            data = head.val
            next_data = head.next.val if head.next is not None else None
            if data == next_data:
                while head is not None and head.val == data:
                    head = head.next
                dummy.next = head


            else:
                head = head.next if head is not None else None
                dummy = dummy.next if dummy is not None else None
        return res.next




        
