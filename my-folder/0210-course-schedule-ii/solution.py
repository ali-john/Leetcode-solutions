class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degrees = [0]*n
        graph = defaultdict(list)

        for course,pre in prerequisites:
            graph[pre].append(course)
            in_degrees[course]+=1
        
        sources = []
        for i,deg in enumerate(in_degrees):
            if deg==0: sources.append(i)
        
        order = []

        while sources:
            node = sources.pop(0)
            order.append(node)
            for next_course in graph[node]:
                in_degrees[next_course]-=1
                if in_degrees[next_course]==0:
                    sources.append(next_course)
        return order if len(order)==n else []



