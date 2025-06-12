# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,next = head)

        prev = dummy
        curr = head

        while curr is not None:
            
            temp = curr
            curr = curr.next
            duplicate = False
            while curr is not None and curr.val == temp.val:
                curr = curr.next
                duplicate = True
            
            if duplicate:
                prev.next = curr
            
            else:
                prev = temp
        return dummy.next


                

            


        
