class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        sequences = set()

        used = [False]*n


        def generate(curr):
            sequences.add(curr)

            for pos,char in enumerate(tiles):
                if not used[pos]:
                    used[pos] = True
                    generate(curr+char)
                    used[pos] = False
        
        generate("")
        return len(sequences) - 1
