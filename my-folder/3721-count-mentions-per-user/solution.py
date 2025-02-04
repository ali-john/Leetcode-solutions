class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        n = numberOfUsers
        mentions = [0]*n

        # sort the inputs
        # also add additional event when user will be activate whenever you encounter an OFFLINE statement
        status = [1]*n # status 1--> active, 0--> deactivate
        
        heap = []
        for event in events:
            
            if event[0]=="OFFLINE":
                new_event = [int(event[1]) + 60,"ACTIVATE",event[2]] # add a custom event to activate back
                heapq.heappush(heap,new_event)
                sorted_event = [int(event[1]),"AOFFLINE", event[2]]
                heapq.heappush(heap,sorted_event)
            else:
                sorted_event = [int(event[1]), event[0], event[2]]
                heapq.heappush(heap,sorted_event)


        while heap:
            _,type, ids  = heapq.heappop(heap)
            #print(f'1 -- type: {type}, ids : {ids}, mentions: {mentions}, status: {status}')
            if type == "ACTIVATE":
                status[int(ids)]=1
            elif type == "MESSAGE":
                if ids == "ALL":
                    for i in range(n): mentions[i]+=1
                elif ids == "HERE":
                    for i in range(n):
                        if status[i]: mentions[i]+=1
                else: # have to parse the ids
                    ids_parsed = list(ids.split(" "))
                    for id in ids_parsed:
                        mentions[int(id[2:])]+=1

            elif type == "AOFFLINE":
                status[int(ids)] = 0

            #print(f' 2 ---- type: {type}, ids : {ids}, mentions: {mentions}, status: {status}')
        return mentions
                    
                    
            
            
                
                
                
            
