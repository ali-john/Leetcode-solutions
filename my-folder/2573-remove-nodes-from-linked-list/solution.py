# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp)
            temp = temp.next
        
        msf = stack[-1].val
        while stack:
            present = stack.pop()
            if present.val<msf:
                if stack:
                    stack[-1].next = present.next
                else:
                    head = present.next
            elif present.val>msf:
                msf = present.val
        return head
