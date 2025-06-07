# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0,None)
        temp = dummyHead

        while l1 is not None and l2 is not None:
            newNode = ListNode(0,None)

            if l1.val <= l2.val:
                newNode.val = l1.val
                l1 = l1.next if l1 is not None else None
            elif l2 is not None:
                newNode.val = l2.val
                l2 = l2.next if l2 is not None else None
            
            temp.next = newNode
            temp = newNode
        
        while l1 is not None:
            newNode = ListNode(l1.val,None)
            temp.next = newNode
            temp = newNode
            l1 = l1.next if l1 is not None else None
        
        while l2 is not None:
            newNode = ListNode(l2.val,None)
            temp.next = newNode
            temp = newNode
            l2 = l2.next if l2 is not None else None
        


        
        return dummyHead.next
