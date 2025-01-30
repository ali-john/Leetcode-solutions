class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007
        
        table = {
            'all': ['a','e','i','o','u'],
            'a': ['e'],
            'e': ['i','a'],
            'i': ['a','e','o','u'],
            'o':['u','i'],
            'u':['a']
        }

        @cache
        def dp(i,char):
           if i==n:
             return 1
           ans = 0
           for nxt in table[char]:
              ans = (ans + dp(i+1,nxt)) % MOD
           return ans
        return dp(0,'all')




            


                

