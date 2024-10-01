class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        left,right = 0, len(cp)-k 
        win_sum = sum(cp[right:])
        total = 0
        max_sum = win_sum
        while right<len(cp):
            win_sum -= cp[right]
            win_sum += cp[left]
            max_sum = max(max_sum,win_sum)
            left+=1
            right+=1
            
        return max_sum
