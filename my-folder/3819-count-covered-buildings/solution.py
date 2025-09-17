class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_table = defaultdict(list)   
        col_table = defaultdict(list)  

        for x, y in buildings:
            row_table[y].append(x)
            col_table[x].append(y)

        # precompute
        row_bounds = {y: (min(xs), max(xs)) for y, xs in row_table.items()}
        col_bounds = {x: (min(ys), max(ys)) for x, ys in col_table.items()}

        covered = 0
        for x, y in buildings:
            min_x, max_x = row_bounds[y]
            min_y, max_y = col_bounds[x]

            if min_x < x < max_x and min_y < y < max_y:
                covered += 1

        return covered
