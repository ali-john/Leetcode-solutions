class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Reach the node just before the "left" position
        for _ in range(left - 1):
            prev = prev.next
        
        # `start` will eventually be the tail of the reversed sublist
        start = prev.next
        then = start.next
        
        # Step 2: Reverse the sublist from "left" to "right"
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next

