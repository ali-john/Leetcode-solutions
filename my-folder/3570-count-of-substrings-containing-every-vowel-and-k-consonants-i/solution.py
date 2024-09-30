from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        n = len(word)
        total = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n-5-k+1):
            vowel_count = 0
            consonant_count = 0
            v = set()
            for j in range(i,n):
                if word[j] in vowels:
                    vowel_count+=1
                    v.add(word[j])
                else:
                    consonant_count+=1

                if len(v)==5 and consonant_count==k:
                    total+=1
        return total
                
                



        

        
        

