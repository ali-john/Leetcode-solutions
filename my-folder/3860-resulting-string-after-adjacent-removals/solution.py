class Solution:
    def resultingString(self, s: str) -> str:
        n = len(s)

        def is_consecutive(a,b):
            if (a== 'a' and b== 'z') or (a=='z' and b == 'a'): return True
            if abs( ord(a) - ord(b) ) == 1: return True
            else: return False
        
        stack = []
        for i in range(n):
            current = s[i]
            if stack and is_consecutive(current, stack[-1]):
                stack.pop()
            else:
                stack.append(current)
        return "".join(stack)


