class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)

        operations = {
            "+": lambda a,b : a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b),
        }

        stack = []

        for char in tokens:
            if char in ["+","-","*","/"]:
                second = stack.pop()
                first = stack.pop()
                operation = operations[char]
                stack.append(operation(first,second))
            else:
                stack.append(int(char))
        
        return int(stack[-1])

