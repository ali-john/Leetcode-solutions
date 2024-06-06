# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = []
        q.append(root)
        left = []
        right = []
        output = []
        j=0
        while(len(q)>0):
            size = len(q)
            sub_list = []
            for i in range(size):
                root = q.pop(0)
                sub_list.append(root.val)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            if j%2 ==0: #0,2,4,6 ...
                right.append(sub_list)
            else:
                sub_list = sub_list[::-1]
                left.append(sub_list)
            j+=1
        if len(right) == len(left):
            for i in range(len(right)):
                output.append(right[i])
                output.append(left[i])
        elif len(right)>len(left):
            start = len(left)
            for i in range(len(left)):
                output.append(right[i])
                output.append(left[i])
            for i in range(start,len(right),1):
                output.append(right[i])
        
        elif len(left)>len(right):
            start = len(right)
            for i in range(len(right)):
                output.append(right[i])
                output.append(left[i])
            for i in range(start,len(left),1):
                output.append(left[i])



        return output
        
