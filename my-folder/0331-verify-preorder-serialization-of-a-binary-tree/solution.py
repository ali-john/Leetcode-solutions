class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        n = len(preorder)

        nodes = preorder.split(',')

        for node in nodes:
            stack.append(node)

            while len(stack)>=3 and stack[-1]=='#' and stack[-2]=='#' and stack[-3]!='#':
                stack.pop()
                stack.pop()
                stack[-1]='#'
        
        return stack[0]=='#' and len(stack)==1

        
            

            





        
