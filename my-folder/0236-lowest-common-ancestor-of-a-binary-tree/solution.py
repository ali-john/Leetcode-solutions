# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lc(self,root,p,q,path,ppath,qpath):
        if root is None:
            return
        path.append(root)
        if root.val == p.val:
            ppath[:] = path
        elif root.val == q.val:
            qpath[:] = path
        self.lc(root.left,p,q,path,ppath,qpath)
        self.lc(root.right,p,q,path,ppath,qpath)
        path.pop()


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        ppath = []
        qpath = []
        self.lc(root,p,q,path,ppath,qpath)
        output = ppath[0]
        l = min(len(ppath),len(qpath))
        for i in range(l):
            if (ppath[i].val==qpath[i].val):
                output = ppath[i]
        return output

        
        
