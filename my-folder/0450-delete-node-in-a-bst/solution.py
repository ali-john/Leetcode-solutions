# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_node(root,parent)->Tuple[Optional['TreeNode'], Optional['TreeNode']]:
            if not root:
                return None, None
            if root.val ==key:
                return (root, parent)
            
            target, parent = find_node(root.right,root)
            if target:
                return target, parent
            
            return find_node(root.left,root)
        
        target,parent = find_node(root,None)
        if target is None:
            return root
        if target.left is None and target.right is None: # leaf node
            if parent is None:
                return None
            if parent.left == target:
                parent.left = None
            else:
                parent.right = None
        
        elif target.right is not None:
            min_node = target.right
            min_parent = target
            while min_node.left:
                min_parent = min_node
                min_node = min_node.left
            target.val = min_node.val
            if min_parent.left == min_node:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right
        elif target.left is not None:
            if parent is None: 
                return target.left
            if parent.left == target:
                parent.left = target.left
            else:
                parent.right = target.left

        return root
