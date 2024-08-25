# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        t = True
        while first and first.next:
            second = first.next
            third = second.next
            second.next = first
            if t:
                head = second
                t = False
            else:
                tmp_1.next = second
            first.next = third
            tmp_1 = first
            first = third

        return head


