# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n+=1
        if n == 1:
            return head
        k = k%n
        if k == 0:
            return head

        dummy = ListNode(0,head)
        skip = n - k
        temp = head
        for _ in range(skip - 1):
            temp = temp.next
        
        beginning = temp.next if temp is not None else None
        head = beginning
        temp.next = None
        while beginning.next is not None:
            beginning = beginning.next
        beginning.next = dummy.next
        return head
