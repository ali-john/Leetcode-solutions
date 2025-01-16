class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)
        if n<d:return -1
        level = [0]*n

        hardest = 0
        for i in reversed(range(n)):
            hardest = max(jobs[i],hardest)
            level[i] = hardest
        @cache
        def dp(i,day):
            if day==d:
                return level[i]
            
            hardest = 0
            best = float('inf')

            for j in range(i,n - (d - day)):
                hardest = max(hardest,jobs[j])
                best = min(best,hardest + dp(j+1,day+1))
            return best
        return dp(0,1)

