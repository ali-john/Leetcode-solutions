# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder,inorder):
            if len(preorder) == 0:
                return None
            root_val = preorder[0]
            root = TreeNode(root_val)
            indx = inorder.index(root_val)
            left = build(preorder[1:1+indx], inorder[:indx])
            right = build(preorder[1+indx:], inorder[indx+1:])

            root.left = left
            root.right = right
            return root
        

        return build(preorder,inorder)
            

