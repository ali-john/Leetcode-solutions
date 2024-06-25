# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(left,right):
            if left>right:
                return None
            
            middle = (left+right)//2
            root = TreeNode(val = nums[middle])
            root.left = construct(left,middle-1)
            root.right = construct(middle+1,right)
            return root
        
        return construct(0,len(nums)-1)
            
            




        
        






        
