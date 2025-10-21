class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        m = len(queries)
        ans = [0]*m
        colors = [0]*n

        curr = 0
        for i, (index, color) in enumerate(queries):
            
            if colors[index] == 0: # if uncolored
                if index - 1>=0 and colors[index - 1] == color: curr+=1
                if index + 1 < n and colors[index + 1] == color: curr+=1
            else: # if already colored
                # remove contribution
                if index - 1 >= 0 and colors[index - 1] == colors[index]: curr-=1
                if index + 1 < n and colors[index + 1] == colors[index]: curr-=1
                # add new contribution if any:
                if index - 1 >= 0 and colors[index - 1] == color: curr+=1
                if index + 1 < n and colors[index + 1] == color: curr+=1

            
            colors[index] = color
            ans[i] = curr
        return ans
            
                    
                    
          


