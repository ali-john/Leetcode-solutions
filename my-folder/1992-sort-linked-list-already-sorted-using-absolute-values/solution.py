# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            if curr.val>curr.next.val:
                temp = curr.next
                curr.next = temp.next
                temp.next = head
                head = temp
            else:
                curr = curr.next
        return head

                




