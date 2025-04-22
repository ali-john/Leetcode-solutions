class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        n = len(rooms)
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        visited = [False]*n

        visited[0] = True
        q = [0]

        while q:
            node = q.pop(0)
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return all(visited) 

