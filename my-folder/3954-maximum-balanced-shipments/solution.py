class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        ans = 0

        max_w = weight[0]

        for i in range(1, n):
            if weight[i] < max_w:
                ans+=1
                max_w = float('-inf')
            else:
                max_w = max(max_w, weight[i])
        return ans
            

            
