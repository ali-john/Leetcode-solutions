class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        t_table = defaultdict(int)
        s_table = defaultdict(int)
        k = n//k
        for i in range(0,n,k):
            t_table[t[i:i+k]] += 1
        
        for i in range(0,n,k):
            sub = s[i:i+k]
            s_table[sub]+=1
        
        return t_table == s_table



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(s)
        # str1 = []
        # str2 = []
        # k = n//k
        # for i in range(0,n,k):
        #     str1.append(s[i:i+k])
        #     str2.append(t[i:i+k])
       
        # str1 = sorted(str1)
        # str2 = sorted(str2)
        # str1 = ''.join(str1)
        # str2 = ''.join(str2)
        # return str1==str2
            
