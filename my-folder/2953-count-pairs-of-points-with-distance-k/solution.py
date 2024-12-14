class Solution:
    def countPairs(self, c: List[List[int]], k: int) -> int:
        data, res = defaultdict(int), 0 

        for p in c:
            x1, y1 = p[0], p[1]
            for x in range(k+1):
                x2, y2 = x1 ^ x, (k-x)^ y1
                if (x2, y2) in data:
                    res+= data[(x2,y2)]
            data[(x1,y1)]+=1
        return res
