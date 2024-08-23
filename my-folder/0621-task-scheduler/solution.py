import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = defaultdict(int)
        for task in tasks:
            table[task]+=1
        
        max_heap = []
        for key,val in table.items():
            heapq.heappush(max_heap,(-val,key))
        
        intervals = 0
        while max_heap:
            wait_list = [] # add waitlisted elements
            can_schedule = n+1
            while can_schedule>0 and len(max_heap)>0:
                intervals+=1
                val,key = heapq.heappop(max_heap)
                if val<-1:
                    wait_list.append((val+1,key))
                can_schedule-=1
            
            for task in wait_list:
                heapq.heappush(max_heap,task)
            
            if max_heap:
                intervals+=can_schedule
        return intervals














