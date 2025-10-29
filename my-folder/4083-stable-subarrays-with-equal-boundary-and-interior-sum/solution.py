class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        prefix = [0]*n
        prefix[0] = capacity[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + capacity[i]
        
        
        table = defaultdict(int)
        for i in range(n):
            pair = (capacity[i],prefix[i])
            table[pair]+=1
        print(table)
        
        ans = 0
        for i in range(n):
            weight = prefix[i] + 2*capacity[i]
            need = (capacity[i], weight)
            table[(capacity[i], prefix[i])]-=1
            if need in table:
                ans+=table[need]
                if i+1 < n and (capacity[i+1],prefix[i+1]) == need:
                    ans-=1 
            
        return ans

        
        print(table)


