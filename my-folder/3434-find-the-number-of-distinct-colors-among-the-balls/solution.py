class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        balls = defaultdict(int)
        colors = defaultdict(set)

        output = [0]*n

        for i,(ball,color) in enumerate(queries):
            # add color to ball
            prev_color = -1
            if (balls[ball]!=0): # if a ball already has some color
                if (balls[ball] == color):
                    output[i] = len(colors)
                    continue
                prev_color = balls[ball]
            balls[ball] = color 

            # add distinct colors:
            colors[color].add(ball)
            # remove previous color
            if prev_color!=-1:
                colors[prev_color].discard(ball)
                if len (colors[prev_color]) == 0:
                    del colors[prev_color]
            output[i] = len(colors)
        return output
                    
                
                
                
