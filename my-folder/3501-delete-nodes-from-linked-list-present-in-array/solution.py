# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = ListNode(0,head)
        prev = dummy
        temp = head
        while temp is not None:
            if temp.val in s:
                prev.next = temp.next
                temp = temp.next
            else:
                temp = temp.next
                prev = prev.next
        return dummy.next



        
        
