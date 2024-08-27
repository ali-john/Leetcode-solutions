class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            in_degree[c1]+=1
        
        sources = []
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                sources.append(i)
        schedule = []
        while sources:
            vertex = sources.pop(0)
            schedule.append(vertex)
            for child in graph[vertex]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    sources.append(child)
    
        if len(schedule)==numCourses:
            return schedule
        else:
            return []


            



        
