# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def is_intersection(headA,headB)->[bool,int,int]:
            tempA = headA
            cnt1 = 0
            tempB = headB
            cnt2 = 0
            while tempA.next:
                tempA = tempA.next
                cnt1+=1
            while tempB.next:
                tempB = tempB.next
                cnt2+=1
            if tempA==tempB:
                return [True,cnt1,cnt2]
            else:
                return [False,cnt1,cnt2]
        
        decision,cnt1,cnt2 = is_intersection(headA,headB)
        if not decision:
            return None
        else:
            start = 0
            if cnt1>cnt2:
                start = cnt1-cnt2
                while start:
                    headA = headA.next
                    start-=1
            else:
                start = cnt2-cnt1
                while start:
                    headB = headB.next
                    start-=1
            while headA:
                if headA==headB:
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next


            


        
