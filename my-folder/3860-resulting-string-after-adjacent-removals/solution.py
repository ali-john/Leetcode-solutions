class Solution:
    def resultingString(self, s: str) -> str:
        n = len(s)

        stack = []

        def is_consecutive(a,b):
            if ( a == 'a' and b == 'z') or (a == 'z' and b == 'a'): return True
            if abs( ord(a) - ord(b) ) == 1:
                return True
            else:
                return False
 
        for i,char in enumerate(s):
            if stack:
                if is_consecutive(stack[-1],char):
                    stack.pop()

                else:
                    stack.append(char)
            else:
                stack.append(char)

        return "".join(stack)
        
                
