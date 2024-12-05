from collections import defaultdict, Counter
from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        for node, parent in enumerate(parents):
            if parent != -1: 
                tree[parent].append(node)
        
        n = len(parents)
        count = Counter()
        def dfs(node):
            subtree_size = 1 
            for child in tree[node]:
                subtree_size += dfs(child)
            count[node] = subtree_size
            return subtree_size

        dfs(0) 
        
        scores = []
        for node in range(n):
            product = 1
            for child in tree[node]:
                product *= count[child]
            remaining = n - count[node]
            if remaining > 0:
                product *= remaining
            
            scores.append(product)

        max_score = max(scores)
        return scores.count(max_score)

