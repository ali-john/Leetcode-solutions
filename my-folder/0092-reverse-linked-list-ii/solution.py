# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # More efficient way would be using two pointers approach
        values = []
        temp = head
        i = 1
        while temp is not None:
            if i>=left and i<=right:
                values.append(temp.val)
            i+=1
            temp = temp.next if temp is not None else None

        i = 1
        temp = head
        j = len(values)-1
        while temp is not None:
            if i>=left and i<=right:
                temp.val = values[j]
                j-=1
            i+=1
            temp = temp.next if temp is not None else None
        return head

            

        
