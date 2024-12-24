class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        n = len(g)
        graph = defaultdict(list)

        for i,l in enumerate(g):
            graph[i] = l
        output = []


        def dfs(curr,path):
            if curr==n-1:
                output.append(path[:])
            
            for nei in graph[curr]:
                path.append(nei)
                dfs(nei,path)
                path.pop()

        dfs(0,[0])
        return output
