# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            dummy = ListNode(-1)
            current = dummy

            while l1 and l2:
                if l1.val<l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1:
                current.next = l1
            if l2:
                current.next = l2
            return dummy.next

        def mergesort(sub_list):
            if not sub_list:
                return None
            if len(sub_list)==1:
                return sub_list[0]
            
            mid = len(sub_list)//2
            left = mergesort(sub_list[:mid])
            right = mergesort(sub_list[mid:])
            return merge(left,right)
        
        if not lists:
            return None
        return mergesort(lists)
