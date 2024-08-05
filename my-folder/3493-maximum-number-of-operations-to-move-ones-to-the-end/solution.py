import copy
class Solution:
    def maxOperations(self, s: str) -> int:
        string = [int(''.join(char)) for char in s]
        n = len(string)
        oc = 0
        zc = 0
        output =0
        for i in range(len(string)-1):
            if string[i]==1:
                oc+=1
            if string[i]==1 and string[i+1]==0:
                output+=oc
        return output





        
        
