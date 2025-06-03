class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        left = 0
        right = n - 1

        ans = float('-inf')
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            ans = max(ans, current_area)

            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        
        return ans

        

        

