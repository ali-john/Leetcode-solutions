class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        k_sum = 0

        for i in range(k):
            k_sum+= calories[i]
        total = 0
        if k_sum>upper:
            total+=1
        elif k_sum<lower:
            total-=1
 
        for i in range(k,n):
            k_sum+=calories[i]
            k_sum-=calories[i-k]

            if k_sum>upper:
                total+=1
            elif k_sum<lower:
                total-=1
        return total

