class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        n = len(g)
        graph = defaultdict(list)

        for i,l in enumerate(g):
            graph[i] = l
        output = []
        
        q = [[0]]
        while q:
            curr_path = q.pop(0)
            curr_node = curr_path[-1]
            for nei in graph[curr_node]:
                temp_path = curr_path.copy()
                temp_path.append(nei)
                if nei == len(graph)-1:
                    output.append(temp_path)
                else:
                    q.append(temp_path)
        return output
                
        

        # def dfs(curr,path):
        #     if curr==n-1:
        #         output.append(path[:])
            
        #     for nei in graph[curr]:
        #         path.append(nei)
        #         dfs(nei,path)
        #         path.pop()

        # dfs(0,[0])
        # return output
