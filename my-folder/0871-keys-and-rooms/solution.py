class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        visited = [False]*len(rooms)
        q = [0]
        visited[0] = True
        while q:
            node = q.pop(0)
            for child in graph[node]:
                if not visited[child]:
                    visited[child] = True
                    q.append(child)
        return all(visited)

