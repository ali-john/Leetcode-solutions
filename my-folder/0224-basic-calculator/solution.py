class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        i=0
        num, sign = 0, 1
        while i<len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            
            elif s[i]=='+':
                stack.append(num*sign)
                num, sign = 0, 1
            elif s[i]=='-':
                stack.append(num*sign)
                num,sign = 0, -1
            elif s[i]=='(':
                stack.append(sign)
                stack.append('(')
                num, sign = 0, 1
            elif s[i]==')':
                stack.append(sign*num)
                num, sign = 0, 1
                sub_sum = 0

                while len(stack)>0:
                    top = stack.pop()
                    if top=='(':
                        sign = stack.pop()
                        break
                    else:
                        sub_sum+=top
                stack.append(sign*sub_sum)
            i+=1
        stack.append(num*sign)
        return sum(stack)







            
            


        
