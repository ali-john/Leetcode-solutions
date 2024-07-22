# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        length = 1
        lastNode = head
        while lastNode.next:
            lastNode = lastNode.next
            length+=1
        
        k = k%length # remove cycles
        if k==0:
            return head
        new_tail = head
        for _ in range(length-k-1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        lastNode.next = head
        return new_head
        
        


        
            


        
