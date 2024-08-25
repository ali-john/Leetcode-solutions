# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        ll = 0
        temp = head
        while temp:
            temp = temp.next
            ll+=1
        
        last = ll - k
        start = k
        startPtr = head
        while head:
            head = head.next
            if start>1:
                start-=1
                startPtr=head
            else:
                break
        
        head = dummyNode.next
        while last>0:
            head=head.next
            last-=1
        
        temp = startPtr.val
        startPtr.val = head.val
        head.val = temp
        return dummyNode.next
                




        
