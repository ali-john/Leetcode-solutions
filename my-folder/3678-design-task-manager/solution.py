class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.table = defaultdict(list)
        self.heap = []
        for task in tasks:
            self.table[task[1]].append(task[2])
            self.table[task[1]].append(task[0])
            heapq.heappush(self.heap,(-task[2],-task[1],task[0]))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.table[taskId].append(priority)
        self.table[taskId].append(userId)
        heapq.heappush(self.heap,(-priority,-taskId,userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.table[taskId][0] = newPriority
        userId = self.table[taskId][1]
        heapq.heappush(self.heap,(-newPriority,-taskId,userId))
        
    def rmv(self, taskId: int) -> None:
        del self.table[taskId]
        
    def execTop(self) -> int:
        if len(self.heap)==0: return -1
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            priority, taskId, userId = -priority, -taskId, userId
            if taskId  in self.table:
                if self.table[taskId][0] == priority and self.table[taskId][1] == userId: # priority is not changed
                    del self.table[taskId]
                    return userId
        if len(self.heap)==0: return -1
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
