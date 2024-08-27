class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
            in_degree[c2]+=1
        
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
    
        return len(schedule)==numCourses





            

            

            




        
