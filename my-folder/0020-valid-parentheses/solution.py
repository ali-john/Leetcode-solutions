class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = collections.deque()
        open_p = ['(','{','[']
        closed_p = [')','}',']']
        output = True
        close_p = False
        for i in range(len(s)):
            val = s[i]
            if val in open_p:
                stack.append(val)
            else:
                close_p = True
                if len(stack)!=0:
                    top = stack.pop()
                    if top == '(':
                        if val != ')':
                            return False
                    elif top=='{':
                        if val != '}':
                            return False
                    elif top=='[':
                        if val != ']':
                            return False
                else:
                    return False

        if close_p:     
            if len(stack)==0:
                return True
            else:
                return False
        else:
            return False

                


        
        
