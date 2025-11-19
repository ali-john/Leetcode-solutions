# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 ==0: return []
        if n ==1: return [TreeNode()]
        table = defaultdict(list)
        base = TreeNode()
        table[1] = [TreeNode()]
        base.left = TreeNode()
        base.right = TreeNode()
        table[3] = [base]

        for i in range(5, n+1,2):
            for j in range(1, n , 2):
                k = i -j - 1
                for node in table[j]:
                    for node2 in table[k]:
                        root = TreeNode()
                        node_c = deepcopy(node)
                        node2_c = deepcopy(node2)
                        root.left = node_c
                        root.right = node2_c
                        table[i].append(root)
        return table[n]
    


       

        
