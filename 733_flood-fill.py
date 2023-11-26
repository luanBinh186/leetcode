class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]
        if source == color:
            return image
        def dfs(image: List[List[int]], source: int, sr: int, sc: int, color: int):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == source:
                # Explore all four directions
                image[sr][sc] = color
                dfs(image, source, sr + 1, sc, color)
                dfs(image, source, sr - 1, sc, color)
                dfs(image, source, sr, sc + 1, color)
                dfs(image, source, sr, sc - 1, color)
            return
        dfs(image, source, sr, sc, color)
        return image