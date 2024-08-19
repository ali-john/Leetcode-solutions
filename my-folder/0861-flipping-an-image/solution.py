class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        def flip(image):
            for i in range(n):
                image[i] = image[i][::-1]
            return image
        
        def invert(image):
            mask = [1]*n
            for i in range(n):
                for j in range(n):
                    image[i][j] = image[i][j]^1
            return image

        flip(image)
        invert(image)
        return image
        
