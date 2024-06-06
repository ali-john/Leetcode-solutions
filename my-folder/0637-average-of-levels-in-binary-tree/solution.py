# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        order = []
        q = []
        q.append((root,0))
        order.append((root.val,0))
    
        while (len(q)>0):
            root,lvl = q.pop(0)
            order.append((root.val,lvl))
    
            if root.left is not None:
                q.append((root.left,lvl+1))
            if root.right is not None:
                q.append((root.right,lvl+1))
                
        level_dict = {}
        for val, lvl in order:
            if lvl not in level_dict:
                level_dict[lvl] = []
            level_dict[lvl].append(val)

        output2 = [mean(vals) for lvl, vals in sorted(level_dict.items())]

        return output2

                
            
            
            
            




        

                
            
            
            
            




        
