class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c:[] for c in range(numCourses)}
        for c1,c2 in prerequisites:
            graph[c1].append(c2)
        
        visited, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        
        for course in list(graph.keys()):
            if dfs(course) == False:
                return []
        return output

            


            



        
