class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        n = len(coords)
        parrallel_x = defaultdict(list) # min, max
        parrallel_y = defaultdict(list) # min, max
        max_x, min_x, max_y, min_y = float('-inf'), float('inf'), float('-inf'), float('inf')

        for i in range(n):
            x, y = coords[i]
            max_x = max(x,max_x)
            min_x = min(x,min_x)
            max_y = max(y,max_y)
            min_y = min(y,min_y)

            if x in parrallel_y:
                parrallel_y[x][0] = min(parrallel_y[x][0], y)
                parrallel_y[x][1] = max(parrallel_y[x][1],y)
            else:
                parrallel_y[x].append(y)
                parrallel_y[x].append(y)
            
            if y in parrallel_x:
                parrallel_x[y][0] = min(parrallel_x[y][0], x)
                parrallel_x[y][1] = max(parrallel_x[y][1],x)
            else:
                parrallel_x[y].append(x)
                parrallel_x[y].append(x)
            
        ans = 0
        # check for parallel to x axis:
    
        for y, val in parrallel_x.items():
            max_base = abs(val[1] - val[0])
            max_height = max(abs(max_y - y) , abs(min_y - y))
            ans = max(max_height*max_base, ans)
        
        # check for parralel to y axis:
        max_height = max(max_x, abs(min_x))
        for x, val in parrallel_y.items():
            max_base = abs(val[1] - val[0])
            max_height = max(abs(max_x - x) , abs(min_x - x))
            ans = max(max_height*max_base, ans)
        
        return ans if ans!=0 else -1



