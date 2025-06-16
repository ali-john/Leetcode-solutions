# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = []
        greater = []

        temp = head
        while temp:
            if temp.val < x:
                lesser.append(temp.val)
            else:
                greater.append(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            val = lesser.pop(0) if len(lesser)>0 else greater.pop(0)
            temp.val = val
            temp = temp.next
        
        return head
