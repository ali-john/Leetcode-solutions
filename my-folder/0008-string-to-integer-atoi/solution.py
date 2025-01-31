class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        clean_s = []
        for i in range(len(s)):
            if s[i]==' ':
                if len(clean_s)==0: continue
                else: break
            else:
                clean_s.append(s[i])

        s = ''.join(clean_s)
        n = len(s)
        positive = False
        negative = False
        clean = []
        for i in range(n):
            if s[i]=='-' or s[i]=='+':
                if len(clean)>0: break
                if negative or positive: break
                elif s[i]=='-': negative = True
                elif s[i]=='+': positive = True
            elif (s[i].isnumeric()):
                clean.append(s[i])
            else:
                break
        if len(clean)==0: return 0
        output = int(''.join(clean))
        if negative:
            if -output<MIN_INT: return -2**31
            else: return -output
        else:
            if output>MAX_INT: return 2**31 -1
            else: return output 
        #return 0




