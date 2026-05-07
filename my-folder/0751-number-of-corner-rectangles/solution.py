class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = defaultdict(int)
        ans = 0
        for row in grid:
            for c1, val in enumerate(row):
                if val:
                    for c2 in range(c1+1, len(row)):
                        if row[c2]:
                            ans+= count[c1,c2]
                            count[c1,c2]+=1
        return ans
