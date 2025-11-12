class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        SUM, x, trees =1, 1, 0
        while True:
            trees = 4 * SUM * (1+2*x)
            if trees >= neededApples:
                return 8*x
            x += 1
            SUM = SUM + x
