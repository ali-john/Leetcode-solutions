# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse_list(node):
            prev = None
            
            while node:
                nextN = node.next
                node.next = prev
                prev = node
                node = nextN
            return prev

        middle = head
        end = head

        while end is not None and end.next is not None:
            end = end.next.next
            middle = middle.next
        
        rightList = reverse_list(middle)
        leftList = head

        while leftList is not None and rightList is not None:
            temp = leftList.next
            leftList.next = rightList
            leftList = temp

            temp = rightList.next
            rightList.next = leftList
            rightList = temp
        
        if leftList is not None:
            leftList.next = None
        


        


        
