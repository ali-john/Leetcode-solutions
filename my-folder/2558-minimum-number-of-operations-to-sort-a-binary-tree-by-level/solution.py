# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = [(root,0)]
        swaps = 0
        processed = set()
        while q:
            node,level = q.pop(0)
            nodes = [node]
            
            if level not in processed:
                j = 0
                while j<len(q) and q[j][1]==level:
                    node_next, _ = q[j]
                    nodes.append(node_next)
                    j+=1
                nodes = [x.val for x in nodes]
                #print(f'current node: {node.val}, nodes: {nodes}')
                mapper = defaultdict(int)
                inverse_mapper = defaultdict(int)
                for i,val in enumerate(nodes):
                    mapper[val] = i
                    inverse_mapper[i] = val

                sorted_nodes = sorted(nodes)
                #print(f'sorted==nodes: {sorted_nodes==nodes}')
                if sorted_nodes!=nodes:
                    for i in range(len(sorted_nodes)):
                        value = sorted_nodes[i]
                        if mapper[value]!=i:
                            prev_index = mapper[value]
                            mapper[value] = i
                            curr = inverse_mapper[i]
                            mapper[curr] = prev_index
                            inverse_mapper[i] = value
                            inverse_mapper[prev_index] = curr
                            swaps+=1
            if node.left: q.append((node.left,level+1))
            if node.right: q.append((node.right,level+1))
            processed.add(level)
        
        return swaps

                    

