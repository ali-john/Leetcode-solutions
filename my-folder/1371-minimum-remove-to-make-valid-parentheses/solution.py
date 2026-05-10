class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        open_stack = []
        close_stack = []

        for i,char in enumerate(s):
            if char == "(":
                open_stack.append(i)
            elif char == ")":
                if len(open_stack) > 0:
                    open_stack.pop(-1)
                else:
                    close_stack.append(i)
        open_stack = set(open_stack)
        close_stack = set(close_stack)
        ans = []
        for i, char in enumerate(s):
            if i in open_stack:
                open_stack.remove(i)
                continue
            elif i in close_stack:
                close_stack.remove(i)
                continue
            else:
                ans.append(char)
        return "".join(ans)


