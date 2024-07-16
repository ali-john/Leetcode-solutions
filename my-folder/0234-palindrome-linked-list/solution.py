# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = []
        second = []

        slow = head
        fast = head
        if head is None or head.next is None:
            return True
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        newPtr = head
        while newPtr!=slow:
            first.append(newPtr.val)
            newPtr = newPtr.next
        
        while newPtr:
            second.append(newPtr.val)
            newPtr = newPtr.next
        
        second = second[::-1]
        if first ==second:
            return True
        elif len(first)>len(second):
            first  = first[:-1]
            if first==second:
                return True 
            else:
                return False
        elif len(first)<len(second):
            second  = second[:-1]
            if first==second:
                return True 
            else:
                return False
        else:
            return False

