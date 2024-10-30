class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        total = 1


        groups = []
        i = 0
        while i<n:
            count = 1
            while i+1<n and word[i]==word[i+1]:
                count+=1
                i+=1
            groups.append(count)
            i+=1
        
        for val in groups:
            if val>1:
                total+=val - 1
        return total


    
        
