# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        temp = head
        while l1 is not None or l2 is not None or carry!=0:
            
            first = l1.val if l1 is not None else 0
            second = l2.val if l2 is not None else 0

            sum = first+second+carry
            digit = sum%10
            carry = sum//10

            output = ListNode(digit)
            temp.next = output
            temp = output

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is  not None else None

        result = head.next
        return result



        

        
