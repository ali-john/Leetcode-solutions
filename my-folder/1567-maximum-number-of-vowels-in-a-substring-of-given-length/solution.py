class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a','e','i','o','u']

        left = 0
        count = 0
        ans = float("-inf")
        for i in range(k):
            if s[i] in vowels:
                count+=1
        ans = max(ans,count)
        
        for right in range(k,n):
            
            if s[right] in vowels:
                count+=1
            
            if s[left] in vowels:
                count-=1
            ans = max(ans,count)
            left+=1
        return ans




