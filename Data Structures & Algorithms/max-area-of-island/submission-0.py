class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        row_size, column_size, = len(grid), len(grid[0])

        def dfs(row, column):
            if row < 0 or row >= row_size or column < 0 or column >= column_size or grid[row][column] == 0:
                return 0

            grid[row][column] = 0

            return 1 + dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column + 1) + dfs(row, column - 1)

        for row in range(row_size):
            for column in range(column_size):   
                if grid[row][column] == 1:
                    max_area = max(dfs(row,column), max_area)

        return max_area