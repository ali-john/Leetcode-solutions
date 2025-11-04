class Solution:
    def minKnightMoves(self, dest_x: int, dest_y: int) -> int:
        visited = set()
        visited.add((0,0))
        directions = [[2,1], [2,-1], [1,2],[1,-2], [-2,1],[-2,-1],[-1,2],[-1,-2]]
        q = [[(0,0), 0]]
        while q:
            coordinate, level = q.pop(0)
            x, y = coordinate[0], coordinate[1]
            if x == dest_x and y == dest_y: return level
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if (new_x, new_y) not in visited:
                    visited.add((new_x,new_y))
                    q.append([(new_x,new_y), level+1])
            
        
            
