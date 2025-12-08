class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        base = sum(technique2)

        deltas = [a-b for a,b in zip(technique1, technique2)]
        deltas.sort(reverse = True)
        
        best = base
        best+= sum( deltas[:k] )

        for delta in deltas[k:]:
            if delta > 0:
                best+=delta
            else:
                break
        return best
        
