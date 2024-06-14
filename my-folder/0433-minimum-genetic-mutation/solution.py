class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = {startGene:0}
        if endGene not in bank:
            return -1
        
        def bfs():
            q = []
            gene,level = startGene,0
            q.append((gene,level))
            visited = set()
            visited.add(gene)
            while q:
                gene,level = q.pop(0)
                if gene == endGene:
                    return level
                for i in range(8):
                    for j in ['A','C','G','T']:
                        new_gene = gene[:i]+j+gene[i+1:]
                        if new_gene not in visited and new_gene in bank:
                            q.append((new_gene,level+1))
                            visited.add(new_gene)
            return -1
        return (bfs())













        return 0

        
