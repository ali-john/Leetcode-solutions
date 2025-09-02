class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        available = [True]*n

        for i in range(n):
            fruit = fruits[i]
            for j in range(n):
                if available[j] and baskets[j]>=fruit:
                    available[j] = False
                    break
        return sum([1 for a in available if a == True])

