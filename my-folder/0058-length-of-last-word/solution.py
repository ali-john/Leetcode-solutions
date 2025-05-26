class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        end_index = -1
        start_index = -1
        for i in reversed(range(n)):
            if s[i] != ' ' and end_index==-1:
                end_index = i
            
            if s[i] == ' ' and end_index!=-1:
                start_index = i
                break
        
        if start_index != -1:
            return end_index - start_index
        
        else:
            return end_index + 1

            

