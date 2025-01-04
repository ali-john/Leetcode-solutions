class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0]*numCourses
        graph = defaultdict(list)
        
        for course,pre in prerequisites:
            graph[pre].append(course)
            in_degree[course]+=1
        
        sources = []
        for i,degree in enumerate(in_degree):
            if degree==0:
                sources.append(i)
        
        schedule = []

        while sources:
            node = sources.pop(0)
            schedule.append(node)

            for child in graph[node]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    sources.append(child)
        return len(schedule)==numCourses


