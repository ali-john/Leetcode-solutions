class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)

        stack = []
        for i in range(n):
            stack.append(s[i])
            if len(stack) >= m and "".join(stack[-m:]) == part:
                for _ in range(m):
                    stack.pop()
        return "".join(stack)

        
        
        
        
        # n = len(s)
        # m = len(part)
        # stack = []

        # def is_match():
        #     return "".join(stack[-m:]) == part

        # for char in s:
        #     stack.append(char)
        #     if len(stack)>=m and is_match():
        #         for i in range(m):
        #             stack.pop()
        # return "".join(stack)

