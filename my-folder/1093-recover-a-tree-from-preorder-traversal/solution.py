# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, t: str) -> Optional[TreeNode]:
        n = len(t)
        stack = []
        index = 0

        while index<n:
            depth = 0
            while index<n and t[index]=="-":
                depth+=1
                index+=1
            value = 0 
            while index<n and t[index].isdigit():
                value = value*10 + int(t[index])
                index+=1
            node = TreeNode(value)

            while len(stack)>depth:
                stack.pop()
            
            if stack:
                if stack[-1].left is None:
                    stack[-1].left  = node
                else:
                    stack[-1].right = node
            stack.append(node)
        
        return stack[0]




