"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect_r(self,root,d):
        if root is None:
            return
        r,val = d[0]
        sub_list = []
        for rt,v in d:
            if v==val:
                sub_list.append(rt)
        
        for i in range(len(sub_list)):
            if i+1<len(sub_list):
                sub_list[i].next = sub_list[i+1]
        
        r,val = d.pop(0)
        root = r
        if root.left is not None:
            d.append((root.left,val+1))
        if root.right is not None:
            d.append((root.right,val+1))

        self.connect_r(root.left,d)
        self.connect_r(root.right,d)


    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        elif root.left is None and root.right is None:
            return root
        d = []
        data = 0
        d.append((root,data))
        self.connect_r(root,d)
        return root

        
        
            
        
        

        

        
