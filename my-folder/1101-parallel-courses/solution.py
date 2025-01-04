class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = [0]*n
        
        for prev, next_ in relations:
            graph[prev-1].append(next_-1)
            in_degree[next_-1]+=1
        
        sources = []
        for i,degree in enumerate(in_degree):
            if degree == 0: sources.append(i)

        count = 0
        studied = 0
        while sources:
            count+=1
            next_sources = []
            for node in sources:
                studied+=1
                for child in graph[node]:
                    in_degree[child]-=1
                    if in_degree[child]==0:
                        next_sources.append(child)
            sources = next_sources
           
        return count if studied==n else -1


