class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def backtrack(openN:int,closedN:int):
            if openN==closedN==n:
                result.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()

        backtrack(0,0)
        return result

        
        
