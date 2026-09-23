class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols=len(grid),len(grid[0])
        visit=set()
        islands=0

        def bfs(r: int,c: int):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col= q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    bfsr,bfsc=row+dr,col+dc
                    if (bfsr in range(rows) and
                    bfsc in range(cols) and
                    grid[bfsr][bfsc]=="1" and
                    (bfsr,bfsc) not in visit):
                        q.append((bfsr,bfsc))
                        visit.add((bfsr,bfsc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1


        return islands

                
