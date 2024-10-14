# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        # Check these conditions:
            # is the height of left and right sub-tree equal?
            # is right and left sub tree also perfect tree
        # if yes:
            # add their sizes in a sizes list
        # sort the sizes list
        # return kth-element from list
        sizes = []
        def dfs(node):
            if not node:
                return (0,True)

            left_node = dfs(node.left)
            right_node = dfs(node.right)

            if (left_node[1] and right_node[1]) and (left_node[0]==right_node[0]): # heights are equal and both are perfect binary trees
                sizes.append(2*left_node[0]+1)
                return (2*left_node[0]+1,True)
            else:
                return (left_node[0]+1, False)
        
        dfs(root)
        sizes = sorted(sizes,reverse=True)
        if len(sizes)<k:
            return -1
        else:
            return sizes[k-1]
       

