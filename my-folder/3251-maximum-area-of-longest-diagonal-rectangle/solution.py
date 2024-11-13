class Solution:
    def areaOfMaxDiagonal(self, dim: List[List[int]]) -> int:
        n = len(dim)

        ans = 0
        longest_dia = 0

        for i in range(n):
            l,w  = dim[i]
            area = (l*w)
            dia = ((l**2)+(w**2))**0.5

            if dia>longest_dia:
                longest_dia = dia
                ans = area
            if dia==longest_dia:
                ans = max(ans,area)
        return ans
