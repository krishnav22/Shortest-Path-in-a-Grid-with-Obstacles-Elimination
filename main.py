from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def is_valid(r, c):
            nonlocal num_rows, num_cols
            return not (r < 0 or c < 0 or r >= num_rows or c >= num_cols)
        num_rows, num_cols = len(grid), len(grid[0])
        myq = deque([(0, 0, k, 0)]) 
        seen = set()
        while myq:
            r, c, shots, steps = myq.popleft()
            if (r, c) == (num_rows-1, num_cols-1):
                return steps
            if (r, c, shots) in seen:
                continue
            seen.add((r, c, shots))
            for next_r, next_c in [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]:
                if not is_valid(next_r, next_c):
                    continue
                if grid[next_r][next_c] == 0:
                    myq.append((next_r, next_c, shots, steps+1))
                else:
                    if shots == 0:
                        continue 
                    myq.append((next_r, next_c, shots-1, steps+1))
        return -1
                
