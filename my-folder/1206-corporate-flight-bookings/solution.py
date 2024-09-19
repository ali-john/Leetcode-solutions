class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        prefix = [0]*n
        b = len(bookings)
        for i in range(b):
            first, last, seats = bookings[i]
            prefix[first-1]+=seats
            if last<n:
                prefix[last]-=seats
            
        
        prev = prefix[0]
        for i in range(1,n):
            prev+=prefix[i]
            prefix[i] = prev


        return prefix
        # table = {}
        # for i in range(1,n+1):
        #     table[i] = 0
        # bb = len(bookings)
        # for i in range(bb):
        #     first,last, book = bookings[i]
        #     table[first]+=book
        #     for r in range(first+1,last+1):
        #         table[r]+=book

        # output = [0]*n
        # for key,val in table.items():
        #     output[key-1] = val
        
        # return output

        


