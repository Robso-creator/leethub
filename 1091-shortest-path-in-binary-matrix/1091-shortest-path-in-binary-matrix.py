"""
https://www.youtube.com/watch?v=YnxUdAO7TAo neetcode
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0,0, 1)]) #r,c and length
        visit = set((0,0))
        direct = [[0,1], [1,0], [1,1], [-1,-1],
                  [0,-1], [-1,0], [1,-1], [-1,1]]
        
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r,c) >= n or grid[r][c]):
                continue
            if r == n -1 and c == n-1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1

#: T: O(n**2) size of the grid
#: S: O(n**2) size of the grid