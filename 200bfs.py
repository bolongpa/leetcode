class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        if not grid: return 0
        col = row = 0
        w, l = len(grid), len(grid[0])
        islands = []
        self.island_cnt = 0
        self.in_island = []  # store 1s that belong to an detected island

        def bfs(i, j, grid):  # find all "1" connected to [i][j]
            queue = [(i, j)]
            visited = [(i, j)]

            while queue:
                print(queue)
                c = queue.pop(0)
                if grid[c[0]][c[1]] == "1":
                    self.in_island.append((c[0], c[1]))
                    visited.append((c[0], c[1]))
                    if c[0] < w - 1 and (c[0] + 1, c[1]) not in visited + queue:
                        queue.append((c[0] + 1, c[1]))
                    if c[0] > 0 and (c[0] - 1, c[1]) not in visited + queue:
                        queue.append((c[0] - 1, c[1]))
                    if c[1] < l - 1 and (c[0], c[1] + 1) not in visited + queue:
                        queue.append((c[0], c[1] + 1))
                    if c[1] > 0 and (c[0], c[1] - 1) not in visited + queue:
                        queue.append((c[0], c[1] - 1))

                else:
                    visited.append((c[0], c[1]))
            self.island_cnt += 1

        for i in range(w):
            for j in range(l):
                if grid[i][j] == "1" and (i, j) not in self.in_island:
                    bfs(i, j, grid)
                    print('#' * 29)

        return self.island_cnt