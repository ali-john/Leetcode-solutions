# class MyCalendar:

#     def __init__(self):
#         self.bookings = []
        

#     def book(self, start: int, end: int) -> bool:
#         for s,e in self.bookings:
#             if not (start>=e or end<=s):
#                 return False
#         self.bookings.append([start,end])
#         return True

# more optimized approach is to use Binary search to search for where you can potentially insert this new interval
class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:
        left = 0
        right = len(self.bookings)

        while left<right:
            mid = (left+right)//2

            if self.bookings[mid][0]<=start:
                left = mid+1
            else:
                right = mid
                
        
        # left now points at potential insertion point, check if insertion is possible and no over lap is there
        if self.intersect(left,start,end):
            return False
        else:
            self.bookings.insert(left,[start,end])
            return True

    def intersect(self,left,start,end):
        return (
            (self.bookings[left-1][1]>start if left>=1 else False) or
            (self.bookings[left][0]<end if left<len(self.bookings) else False)
        )

        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
