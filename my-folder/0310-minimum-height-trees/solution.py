class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph = defaultdict(list)
        degrees = [0]*n
        # fill graph
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degrees[node1]+=1
            degrees[node2]+=1
        # store all leaf nodes
        sources = []
        for i in range(len(degrees)):
            if degrees[i]==1: 
                sources.append(i)
        
        total_nodes = n
        while total_nodes>2:
            leaves = len(sources)
            total_nodes-=leaves
            for i in range(leaves):
                vertex = sources.pop(0)
                for neighbour in graph[vertex]:
                    degrees[neighbour]-=1
                    if degrees[neighbour]==1:
                        sources.append(neighbour)
        return sources
            

        
