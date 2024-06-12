class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        if len(prerequisites)==0:
            return True
        for c1,c2 in prerequisites:
            if c1 not in graph:
                graph[c1] = []
            if c2 not in graph:
                graph[c2] = []
            graph[c1].append(c2)
        
        visited = set()
        def dfs(node):
            if graph[node]==[]:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            graph[node] = []
            return True
        
        keys = list(graph.keys())
        for course in keys:
            if not dfs(course):
                return False
        return True
        
        



            
            



            
                    
            
        return not(bfs(graph))


            

            

            




        
