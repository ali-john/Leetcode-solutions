class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)

        gen = set()
        used = [False]*n

        def generate(inp):
            gen.add(inp)
            for pos, char in enumerate(tiles):
                if not used[pos]:
                    used[pos] = True
                    generate(inp+char)
                    used[pos] = False
        generate("")
        print(gen)
        return len(gen) - 1




