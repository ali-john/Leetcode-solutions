class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degrees = [0]*n
        for u,v in edges:
            degrees[v]+=1
        
        found_one = False
        possible = -1
        for i,degree in enumerate(degrees):
            if degree ==0:
                if found_one:
                    return -1
                else:
                    found_one = True
                    possible = i

        if found_one:
            return possible
