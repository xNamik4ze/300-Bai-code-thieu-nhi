class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = {}
        for row in grid:
            r_tuple = tuple(row)
            if r_tuple in row_counts:
                row_counts[r_tuple] += 1
            else:
                row_counts[r_tuple] = 1
        count = 0
        for c in range(len(grid)):
            column = tuple(grid[r][c] for r in range(len(grid)))
            count += row_counts.get(column, 0)
        return count