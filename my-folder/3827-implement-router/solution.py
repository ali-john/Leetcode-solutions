class Router:

    def __init__(self, memoryLimit: int):
        self.deque = deque()
        self.max_memory = memoryLimit
        self.packets = set()
        self.destinations = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination, timestamp)
        if packet in self.packets: # already exists
            return False
        if len(self.deque) >= self.max_memory:
            self.forwardPacket()
            
        self.deque.append(packet)        
        self.packets.add(packet)
        if destination not in self.destinations:
            self.destinations[destination] = SortedList()
        self.destinations[destination].add(timestamp)
        return True
            
    
    def forwardPacket(self) -> List[int]:
        if len(self.deque) > 0:
            packet = self.deque.popleft()
            self.packets.remove(packet)
            packet = list(packet)
            self.destinations[packet[1]].remove(packet[2])
            return packet
        else: return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destinations:
            return 0
        l = self.destinations[destination]
        start = bisect_left(l, startTime)
        end = bisect_right(l, endTime)
        return end - start

        
        
        
        
        
        # l = [p_timestamp for p_source, p_destination, p_timestamp in self.deque  if p_destination == destination ] 

        # ans = 0
        # for time in l:
        #     if startTime <= time <= endTime: ans+=1
        # return ans
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
