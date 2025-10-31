class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        cost = sorted(zip(difficulty,profit))
        pref = []
        best = 0
        for d,p in cost:
            if p > best: best = p
            pref.append((d,best))
        worker.sort()
        ans = 0
        i = 0
        for w in worker:
            while i < len(pref) and pref[i][0] <= w:
                i+=1
            if i > 0:
                ans+=pref[i - 1][1]
        return ans





        ans = 0
        for work in worker:
            curr = 0
            for c in cost:
                if c[0] <= work:
                    curr = max(curr, c[1])
            ans+=curr
        return ans
