# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        table = defaultdict(list)

        for info in descriptions:
            node, child, is_left = info[0], info[1], info[2]
            new_node = None
            if node in table:
                new_node = table[node][0]
            else:
                new_node = TreeNode()
                new_node.val = node
                table[node] = [new_node,-1]

            if child in table:
                if is_left:
                    new_node.left = table[child][0]
                    table[child][1] = node
                else:
                    new_node.right = table[child][0]
                    table[child][1] = node
            else:
                child_node = TreeNode()
                child_node.val = child
                table[child] = [child_node,node]
                if is_left:
                    new_node.left = child_node
                else:
                    new_node.right = child_node
        for key,val in table.items():
            if val[1]==-1:
                return val[0]
        

