class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        
        n = len(events)

        val = (events[0][0],events[0][1]) # index, value
        
        for i in range(1,n):
            if (events[i][1] - events[i-1][1]) > val[1]:
                val = (events[i][0], events[i][1]-events[i-1][1])
            elif (events[i][1] - events[i-1][1]) == val[1] and events[i][0]<val[0]:
                val = (events[i][0], events[i][1]-events[i-1][1])

        return val[0]
        
            
            
            
       
