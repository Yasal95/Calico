from collections import deque

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = input().strip()
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))

        # where is each button?
        pos = {}
        for r in range(n):
            for c in range(m):
                pos[grid[r][c]] = (r, c)

        # drift: U = -1,0  D = +1,0  L = 0,-1  R = 0,+1
        drift = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        # my 5 actions: stay + 4 moves
        actions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

        L = len(s)
        cur_r, cur_c = 0, 0
        phase = 0  # how many actions we have done % L
        total = 0

        for button in range(1, n * m + 1):
            tr, tc = pos[button]
            if (cur_r, cur_c) == (tr, tc):
                continue

            # BFS from current pos with current phase
            q = deque()
            q.append((cur_r, cur_c, 0))  # r, c, steps from here
            visited = set()
            visited.add((cur_r, cur_c, phase))
            found = None

            while q:
                r, c, d = q.popleft()
                # drift for this step
                dr, dc = drift[s[(phase + d) % L]]

                for ar, ac in actions:
                    nr = (r + ar + dr) % n
                    nc = (c + ac + dc) % m
                    nd = d + 1
                    if (nr, nc) == (tr, tc):
                        found = nd
                        q.clear()
                        break
                    key = (nr, nc, (phase + nd) % L)
                    if key not in visited:
                        visited.add(key)
                        q.append((nr, nc, nd))
                if found is not None:
                    break

            total += found
            phase = (phase + found) % L
            cur_r, cur_c = tr, tc

        print(total)

if __name__ == "__main__":
    solve()
  output:
5
3
