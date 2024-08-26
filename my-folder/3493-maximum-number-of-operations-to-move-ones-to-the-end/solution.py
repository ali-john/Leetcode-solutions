import copy
class Solution:
    def maxOperations(self, s: str) -> int:
        oc = 0
        operations = 0
        for i in range(len(s)-1):
            if s[i] == '1':
                oc+=1
            if s[i]=='1' and s[i+1]=='0':
                operations+=oc
        return operations    




        
        
