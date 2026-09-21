class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        row_size, column_size = len(image), len(image[0])

        def dfs(row, column):
            if row < 0 or row >= row_size or column < 0 or column >= column_size or image[row][column] != original:
                return

            image[row][column] = color
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        dfs(sr, sc)
        return image    

