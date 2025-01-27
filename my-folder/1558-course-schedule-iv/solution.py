class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], q: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degrees = [0]*n
        for c1,c2 in pre:
            graph[c1].append(c2)
            in_degrees[c2]+=1
        sources = []
        output_list = defaultdict(set)
        #print(output_list)
        for i,degree in enumerate(in_degrees):
            if degree==0:
                sources.append(i)
        for node in range(n):
            output_list[node] = set()
        
        while sources:
            node = sources.pop(0)
            for child in graph[node]:
                in_degrees[child]-=1
                output_list[child].add(node)
                for nei in output_list[node]:
                    output_list[child].add(nei)
                if in_degrees[child]==0:
                    sources.append(child)
        ans = []
        for q1,q2 in q:
            if q1 in output_list[q2]:
                ans.append(True)
            else: ans.append(False)
        return ans
