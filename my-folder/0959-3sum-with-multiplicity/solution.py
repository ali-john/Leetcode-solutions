class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ans = 0
        MOD = 10**9 + 7
        table = Counter(arr)
        st = set()


        for i in range(101):
            for j in range(101):
                k = target - i - j
                if k < j or k > 100:
                    continue
                if table[k] == 0:
                    continue
                s = i + j + k
                elements = tuple(sorted([i,j,k]))
                if elements in st: continue
                if s == target and i in table and j in table and k in table:
                    if i != j and j != k and i!=k:
                        temp = ( table[i] * table[j] * table[k] ) % MOD
                        ans = (ans + temp) % MOD
                    if i == j and j == k:
                        temp = comb(table[i], 3)
                        ans = (ans + temp) % MOD
                    if i == j and j!=k:
                        c = comb(table[i], 2)
                        temp =  ( c * table[k] ) % MOD
                        ans = (ans + temp) % MOD
                    if i == k and j!=k:
                        c = comb(table[i], 2)
                        temp =  ( c * table[j] ) % MOD
                        ans = (ans + temp) % MOD
                    if j == k and i!=k:
                        c = comb( table[j], 2)
                        temp =  ( c * table[i] ) % MOD
                        ans = (ans + temp) % MOD
                    st.add(elements)
        return ans
                        

                        
        

