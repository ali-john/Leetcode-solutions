# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        head = ListNode(0,None)
        temp = head

        while l1 is not None or l2 is not None or carry!=0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum = val1 + val2 + carry
            digit = sum%10
            carry = sum//10

            newNode = ListNode(digit)
            temp.next = newNode
            temp = newNode

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        return head.next
        




        # node1 = l1
        # node2 = l2
        # output = []

        # carry = 0

        # while node1 is not None and node2 is not None:
        #     total = (node1.val + node2.val + carry)
        #     if total < 10:
        #         output.append(total)
        #         carry = 0
        #     else:
        #         current = total - 10
        #         carry = 1
        #         output.append(current)
        #     node1 = node1.next
        #     node2 = node2.next

        # while node1 is not None:
        #     total = (node1.val  + carry)
        #     if total < 10:
        #         output.append(total)
        #         carry = 0
        #     else:
        #         current = total - 10
        #         carry = 1
        #         output.append(current)
        #     node1 = node1.next
        
        # while node2 is not None:
        #     total = (node2.val + carry)
        #     if total < 10:
        #         output.append(total)
        #         carry = 0
        #     else:
        #         current = total - 10
        #         carry = 1
        #         output.append(current)
        #     node2 = node2.next
        # if carry:
        #     output.append(carry)
        
        # dummy = ListNode(0,None)
        # head = ListNode(0,None)
        # dummy.next = head
        # n = len(output)
        # for i in range(len(output)):
        #     head.val = output[i]
        #     if i == n - 1:
        #         break
        #     temp = ListNode(0,None)
        #     head.next = temp
        #     head = temp
        # return dummy.next


