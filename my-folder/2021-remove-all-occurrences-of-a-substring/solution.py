class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)

        stack = []
        def is_match():
            return "".join(stack[-m:]) == part

        for i,char in enumerate(s):
            stack.append(char)

            if len(stack)>=m and is_match():
                for _ in range(m):
                    stack.pop()
        
        return "".join(stack)


