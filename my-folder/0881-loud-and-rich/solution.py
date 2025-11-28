class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i:[] for i in range(n)}
        for u, v in richer:
            graph[v].append(u)
        
        table = {}
        for index, level in enumerate(quiet):
            table[level] = index
        
        #print(graph)
        @cache
        def dfs(person):
            quietness = quiet[person]

            for child in graph[person]:
                level = dfs(child)
                quietness = min(level, quietness)
            return quietness
        
        answer = [i for i in range(n)]
        for i in range(n):
            level = dfs(i)
            person = table[level]
            answer[i] = person
        return answer

