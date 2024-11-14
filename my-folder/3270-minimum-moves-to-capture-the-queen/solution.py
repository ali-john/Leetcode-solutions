class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        bishop = c+d
        queen = e+f
        rook = a+b

        if queen==bishop:
            if rook==bishop: # same diagonal, now check if it is in between or not
                if (a>c and a<e) or (b>d and b<f):
                    return 2
            return 1

        if c-d == e-f:# lower diagonal
            print('lower diagonal')
            if a-b==e-f:# rook can be in between
                print('in between')
                if (a>e and a<c) or (a>c and a<e):
                    return 2
                # if (a>c and a<e) or (b>d and b<f):
                #     return 2   
            return 1
            
        if (a==e or b==f):
            if c==a:
                if (d>b and d<f) or (d>f and d<b): #in between
                    return 2
            elif d==b:
                if (c>e and c<a) or (c>a and c<e):
                    return 2
            return 1
            
         
        return 2
        
