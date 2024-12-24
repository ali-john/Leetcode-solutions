class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for start,end in sorted(tickets,reverse = True):
            graph[start].append(end)
        
        output = []
        def dfs(curr):
            while graph[curr]:
                dfs(graph[curr].pop())
            output.append(curr)

        dfs("JFK")
        return output[::-1]
