class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s)


        output = []
        vowels = ['a', 'e', 'i', 'o','u']

        hit_consonant = False
        for i in range(n-1, -1, -1):
            if s[i] in vowels:
                continue
            else:
                output.append(s[:i+1])
                break
        return "".join(output)
        
            
                
            
            
                
                
            
