# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)

        def build_levels(root, level):
            queue = [(root,level)]
            while queue:
                node, level = queue.pop(0)
                levels[level].append(node.val)
                if node.left is not None:
                    queue.append((node.left, level+1))
                if node.right is not None:
                    queue.append((node.right, level+1))
            return 
        build_levels(root,0)
        swaps = 0
        # process each level
        for lvl, val in levels.items():
            sorted_val = sorted(val)
            actual_counter = {value : i for i,value in enumerate(val) }
            updated_counter = {i: value for i, value in enumerate(val) }
            for i, num in enumerate(sorted_val):
                current_val = updated_counter[i]
                if current_val != num:
                    current_val_updated_index = actual_counter[num]
                    updated_counter[current_val_updated_index] = current_val
                    updated_counter[i] = num
                    actual_counter[num] = i
                    actual_counter[current_val] = current_val_updated_index
                    swaps+=1
        return swaps

                








        
        
        
