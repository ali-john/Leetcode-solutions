class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_count = float("inf")
        whites = 0
        blacks = 0
        left = 0
        for right in range(n):
            if blocks[right]=='W':
                whites+=1
            else:
                blacks+=1
            
            if right-left+1==k:
                min_count = min(min_count,whites)
                if blocks[left]=='W':
                    whites-=1
                else:
                    blacks-=1
                left+=1
        return min_count
