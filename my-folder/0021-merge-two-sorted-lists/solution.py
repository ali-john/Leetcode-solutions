# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        head = output #store starting point of resultant list
        temp = output
        l1 = list1
        l2 = list2
        first = l1.val if l1 is not None else None
        second = l2.val if l2 is not None else None

        while l1 is not None or l2 is not None:
            if first is not None and second is not None:
                if first<second:
                    NewNode = ListNode(first)
                    temp.next = NewNode
                    temp = NewNode
                    l1 = l1.next if l1 is not None else None
                    first = l1.val if l1 is not None else None
                elif second<first:
                    NewNode = ListNode(second)
                    temp.next = NewNode
                    temp = NewNode
                    l2 = l2.next if l2 is not None else None
                    second = l2.val if l2 is not None else None
                else:
                    NewNode1 = ListNode(first)
                    NewNode2 = ListNode(second)
                    NewNode1.next = NewNode2
                    temp.next = NewNode1
                    temp = NewNode2
                    l1 = l1.next if l1 is not None else None
                    first = l1.val if l1 is not None else None
                    l2 = l2.next if l2 is not None else None
                    second = l2.val if l2 is not None else None

            else: # One list is completed. Add the other now
                if l1 is None:
                    while l2 is not None:
                        NewNode = ListNode(second)
                        temp.next = NewNode
                        temp = NewNode
                        l2 = l2.next if l2 is not None else None
                        second = l2.val if l2 is not None else None
                else:
                    while l1 is not None:
                        NewNode = ListNode(first)
                        temp.next = NewNode
                        temp = NewNode
                        l1 = l1.next if l1 is not None else None
                        first = l1.val if l1 is not None else None
                    
        
        result = head.next
        return result






        
