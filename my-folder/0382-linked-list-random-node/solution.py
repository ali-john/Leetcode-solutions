# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            self.n+=1

    def getRandom(self) -> int:
        index = random.randint(0,self.n-1)
        temp = self.head
        i = 0
        while temp:
            if i==index:
                return temp.val
            i+=1
            temp = temp.next
        




        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
