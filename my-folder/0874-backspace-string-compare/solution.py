class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getChar(string,index):
            hash_count = 0
            while index>=0:
                if string[index]=='#':
                    hash_count+=1
                elif hash_count>0:
                    hash_count-=1
                else:
                     break
                index-=1
            return index
        
        ptrOne = len(s)-1
        ptrTwo = len(t)-1

        while ptrOne>=0 or ptrTwo>=0:
            i = getChar(s,ptrOne)
            j = getChar(t,ptrTwo)

            if i<0 and j<0:
                return True
            elif i<0 or j<0:
                return False
            elif s[i]!=t[j]:
                return False

            ptrOne = i-1
            ptrTwo = j-1

        return True
            
                
            




        
