class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        n = len(nodes)
        if nodes[0][1]!=-1: # if first node is not root, then in correct pre-order traversal
            return False
        
        stack = [nodes[0]]

        for i in range(1,n):
            while stack and stack[-1][0]!=nodes[i][1]:
                stack.pop()
            if not stack:
                return False 
            else:
                stack.append(nodes[i])
        return True




# Brute force --- Construct tree and compare pre-order traversal
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.right = right
        self.left = left
        self.val = val

class Solution1:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        pre_order_list = []
        def pre_order(root):
            if not root:
                return
            pre_order_list.append(root.val)
            pre_order(root.left)
            pre_order(root.right)
            
        n = len(nodes)
        table = defaultdict()
        root = TreeNode()
        root.val = nodes[0][0]
        table[root.val] = root

        for i in range(1,n):
            new_node = TreeNode()
            new_node.val = nodes[i][0]
            if nodes[i][1] not in table:
                return False
            parent = table[nodes[i][1]]
            table[new_node.val] = new_node
            if parent.left is None and parent.right is None:
                parent.left = new_node
            elif parent.left is not None and parent.right is None:
                parent.right = new_node
            elif parent.left is None and parent.right is not None:
                return False
        
        pre_order(root)
        given = []
        for i in range(n):
            given.append(nodes[i][0])
        
        return given==pre_order_list
    

            


        
