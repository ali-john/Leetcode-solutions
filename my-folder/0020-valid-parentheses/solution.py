class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        

        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) > 0:
                    if char == ')' and stack[-1]!= '(':
                        return False
                    elif char == '}' and stack[-1]!='{': return False
                    elif len(stack)>0 and char == ']' and stack[-1]!='[': return False
                    else:
                        stack.pop(-1)
                else:
                    return False
        return len(stack)==0
