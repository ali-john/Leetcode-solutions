# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.map = defaultdict(int)
        root.val = 0
        self.map[0] = 1
        def build(self,node):
            if not node: return
            if node.left is not None:
                val = 2*node.val + 1
                node.left.val = val
                self.map[val] = 1
            if node.right is not None:
                val = 2*node.val + 2
                node.right.val = val
                self.map[val] = 1
            
            build(self,node.left)
            build(self,node.right)
        build(self,root)


    def find(self, target: int) -> bool:
        if target in self.map:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
