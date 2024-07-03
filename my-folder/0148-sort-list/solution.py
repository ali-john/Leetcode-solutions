# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


        def merge(l1,l2):
            dummy = ListNode(-1)
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            if l1:
                current.next = l1
            if l2:
                current.next = l2
            
            return dummy.next


        def mergesort(head):
            if head is None or head.next is None:
                return head
            slow = head
            fast = head
            prev = slow
            while fast and fast.next:
                fast=fast.next.next # two steps
                prev = slow # one node before middle
                slow = slow.next # points to middle to array
            if prev:
                prev.next = None
            # call on left list
            first_half = mergesort(head)
            # call on right list
            second_half = mergesort(slow)
            return merge(first_half,second_half)
        
        return mergesort(head)
            



        

        
