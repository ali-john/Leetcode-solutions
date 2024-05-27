# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        from queue import Queue
        dummyNode = ListNode(0,head)
        dummy = dummyNode

        if head is None or head.next is None:
            return head
        smaller = Queue()
        larger = Queue()
        temp = head
        while temp is not None:
            if temp.val >= x:
                larger.put(temp.val)
            else:
                smaller.put(temp.val)
            temp = temp.next if temp is not None else None
        
        temp = head
        while temp is not None:
            if smaller.empty() is False:
                temp.val = smaller.get()
            else:
                temp.val = larger.get()
            temp = temp.next if temp is not None else None
        return head
            

        
        
