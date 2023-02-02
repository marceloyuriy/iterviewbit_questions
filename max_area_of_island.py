import collections
class Solution: 
    def maxAreaOfIsland(self, grid):
        '''My solution based on number_islands algorithm
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs (r, c): 
            curr_area = 0
            q = collections.deque() #Queue to storage the values visited
            visited.add((r,c))
            q.append((r,c))
            curr_area += 1
            while q: 
                row,col = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    row, col = row + dr, col + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row ,col) not in visited:
                        q.append((row,col))
                        curr_area += 1
                        visited.add((row,col))
            return curr_area
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = bfs (r,c)
                    if curr_area >= max_area:
                        max_area = curr_area
        return max_area
        '''
        #NeetCode solution using dfs
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area