class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:


        min_val = float('inf')
        min_index = float('inf')

        for i, cap in enumerate(capacity):
            if cap >= itemSize:
                if cap < min_val:
                    min_index = i
                    min_val = cap
        
        return min_index if min_index!=float('inf') else -1




        
