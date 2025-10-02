class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1000000007
        n = len(points)
        # GROUP BY HORIZONTAL LINES
        table = defaultdict(int)
        for x,y in points:
            table[y]+=1
        
        # PRECOMPUTE TOTAL SUM
        k = list(table.keys())
        total = math.comb(table[k[0]], 2) % MOD
        precomp = [0]*len(k)
        precomp[0] = total
        for i in range(1,len(k)):
            total+=math.comb(table[k[i]], 2) % MOD
            precomp[i] = total
        # PRECOMPUTE EVERY Y VALUE COMBINATION
        per_val = defaultdict(int)
        for key in k:
            per_val[key] = math.comb(table[key],2) % MOD
        
        ans = 0
        for i in range(len(k)):
            ans+= ( per_val[k[i]] * (precomp[-1] - precomp[i]) ) % MOD
            
        return ans%MOD
