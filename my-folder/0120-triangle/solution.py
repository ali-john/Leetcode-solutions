class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(dp(row+1, col), dp(row+1, col+1))
            return path
        return dp(0,0)
