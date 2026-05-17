class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        n = len(hBars)
        m = len(vBars)
        hBars = sorted(hBars)
        vBars = sorted(vBars)

        hmax, vmax = 1, 1
        hcurr, vcurr = 1, 1

        for i in range(1, n):
            if hBars[i] == hBars[i-1] + 1:
                hcurr+=1
            else:
                hcurr = 1
            hmax = max(hmax, hcurr)
        
        for i in range(1,m):
            if vBars[i] == vBars[i-1]+1:
                vcurr+=1
            else:
                vcurr = 1
            vmax = max(vmax, vcurr)
        side = min(vmax, hmax) + 1
        return side**2
