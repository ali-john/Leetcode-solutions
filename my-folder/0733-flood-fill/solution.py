class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        initial = image[sr][sc]


        def dfs(r,c,visited):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((r,c))
            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]
                if new_r>=0 and new_r<rows and new_c>=0 and new_c<cols and image[new_r][new_c]==initial:
                    if ((new_r,new_c) not in visited):
                        dfs(new_r,new_c,visited)


        visited = set()
        visited.add((sr,sc))
        dfs(sr,sc,visited)

        for r,c in visited:
            image[r][c] = color
        return image
