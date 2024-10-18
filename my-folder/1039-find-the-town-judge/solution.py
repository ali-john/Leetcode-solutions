class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}

        for u,v in trust:
            graph[u].append(v)
        
        ans  = -1
        possibles = []
        for u,v in graph.items():
            print(f'u: {u}, v:{v}')
            if len(v)==0:
                possibles.append(u)
        if len(possibles)>1 or len(possibles)==0:
            return -1
        else:
            ans = possibles[0]
            for i in range(1,n+1):
                if i==ans:
                    continue
                else:
                    if ans not in graph[i]:
                        return -1
            return ans
