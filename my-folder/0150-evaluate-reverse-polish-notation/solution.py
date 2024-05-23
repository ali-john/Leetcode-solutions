class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for i in range(len(tokens)):
            if tokens[i] == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                ans = num1+num2
                stack.append(ans)

            elif tokens[i] == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                ans = int(num2/num1)
                stack.append(ans)
            
            elif tokens[i] == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                ans = num2 - num1
                stack.append(ans)

            elif tokens[i] == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                ans = (num1*num2)
                stack.append(ans)

            else: # its a number
                stack.append(int(tokens[i]))
        return stack[-1]


        
