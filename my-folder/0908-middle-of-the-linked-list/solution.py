# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp , n = head, 0
        while temp:
            temp = temp.next
            n+=1
        
        n = n//2
        temp = head
        while n:
            temp = temp.next
            n-=1
        return temp


        
