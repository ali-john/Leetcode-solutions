# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def is_same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            
            return is_same(p.right,q.right) and is_same(p.left,q.left)
        
        return is_same(p,q)


        # BFS Approach
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False

        # def bfs(node) -> list:
        #     que = [node]
        #     ans = []
        #     while que:
        #         top = que.pop(0)
        #         ans.append(top.val)

        #         if top.left is not None:
        #             que.append(top.left)
        #             ans.append(top.left.val)
        #         else:
        #             ans.append("#")
                
        #         if top.right is not None:
        #             que.append(top.right)
        #             ans.append(top.right.val)
        #         else:
        #             ans.append("#")
            
        #     return ans
        
        # p_l = bfs(p)
        # q_l = bfs(q)
        # print(p_l)
        # print(q_l)
        # return p_l == q_l
            


        
