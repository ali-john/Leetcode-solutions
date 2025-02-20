class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        max_line = 0
        for x,y,l in squares:
            max_line = max(max_line,y+l)
        
        left = 0
        right = max_line

        def get_diff(line):
            top, bottom = 0, 0 
            for x,y,l in squares:
                area = l*l
                y1, y2 = y, y+l

                if y1>=line and y2>=line:
                    top+=area
                elif y1<line and y2<line:
                    bottom+=area
                else:
                    top+= (y2-line)*l
                    bottom+= (line-y1)*l
            return top - bottom

        

        while right - left >= pow(10,-5):
            mid = (right+left) / 2
            if get_diff(mid)>0: # move line down
                left = mid
            else: # move line up
                right = mid
        return left
            
        

