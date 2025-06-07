# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head
        
        
        stack = []
        temp = head
        i = 1

        while temp is not None:
            if left <= i <= right:
                stack.append(temp.val)
            i+=1
            temp = temp.next
        
        temp = head
        i = 1
        while temp is not None:
            if left <= i <= right:
                temp.val = stack.pop()
            temp = temp.next
            i+=1
        temp = head

        # while temp:
        #     print(temp.val)
        #     temp = temp.next
        return head


        
        # i = 1
        # left_node = None
        # right_node = None
        # starting_node = None


        # temp = head
        # while temp:
        #     if i == left:
        #         starting_node = temp
        #     elif i == right:
        #         right_node = temp.next
            
        #     if starting_node is None:
        #         left_node = temp
        #     i+=1
        #     temp = temp.next if temp else None
        
        # slow = starting_node
        # fast = starting_node.next
        # while slow:


