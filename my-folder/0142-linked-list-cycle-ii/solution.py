# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cycle = False

        slow = head
        fast = head
        
        def getCycleLen(slow):
            newPtr = slow.next
            count = 1
            while newPtr!=slow:
                newPtr = newPtr.next
                count+=1
            return count

        def findStart(cycle_len):
            ptr1 = head
            ptr2 = head
            while cycle_len:
                ptr1 = ptr1.next
                cycle_len-=1
            
            while ptr1!=ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
            

        cycle_len = 0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                cycle = True
                cycle_len = getCycleLen(slow)
                break
        
        return findStart(cycle_len) if cycle else None
                
                
            



        
