class EventManager:

    def __init__(self, events: list[list[int]]):
        self.pq = []
        self.mapper = defaultdict()
        for eventID, priority in events:
            self.pq.append([-priority, eventID])
            self.mapper[eventID] = priority
        heapq.heapify(self.pq)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.mapper[eventId] = newPriority
        heapq.heappush(self.pq, [-newPriority, eventId])

    def pollHighest(self) -> int:
        while self.pq:
            priority, eventID = heapq.heappop(self.pq)
            priority = -priority
            if eventID in self.mapper and self.mapper[eventID] == priority:
                del self.mapper[eventID]
                return eventID
        return -1

        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
