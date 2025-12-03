class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        # O --> red
        # 1 --> blue
        for start, end in redEdges:
            graph[start].append((end, 0))
        for start,end in blueEdges:
            graph[start].append((end, 1))
        
        def bfs():
            distances = [-1]*n
            distances[0] = 0

            visited = set()
            visited.add((0, 0))
            visited.add((0, 1))
            
            q = [(0, 0, 0)] # node, steps, last_color
            q.append((0, 0, 1))

            while q:
                node, steps, last_color = q.pop(0)
                
                for nei, nei_color in graph[node]:
                    if last_color!=nei_color and (nei, nei_color) not in visited:
                        if distances[nei] == -1:
                            distances[nei] = steps + 1
                        visited.add((nei,nei_color))
                        q.append((nei, steps+1, nei_color))
                
            return distances
        return bfs()
        
        



            

                
                
                






