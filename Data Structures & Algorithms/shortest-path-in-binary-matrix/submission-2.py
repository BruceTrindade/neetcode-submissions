class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid)
        if grid[0][0] or grid[size - 1][size- 1]:
            return -1

        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        direct = [(0, 1), (1, 0), (0, -1), 
        (-1, 0), (1, 1), 
        (-1, -1), (1, -1), (-1, 1)] 

        while q:
            row, column, lenght = q.popleft()
            if row == size - 1 and column == size - 1:
                return lenght

            for dr, dc in direct:
                next_row, next_column = row + dr, column + dc
                if (0 <= next_row < size and 0 <= next_column < size and grid[next_row][next_column] == 0 and (next_row, next_column) not in visit):
                    q.append((next_row, next_column, lenght + 1))
                    visit.add((next_row, next_column))

        return -1                