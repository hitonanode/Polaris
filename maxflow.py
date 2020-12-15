# example: <https://yukicoder.me/submissions/592401>
from collections import deque

class MaxFlow:
    def __init__(self, N: int) -> None:
        self.N = N
        self.edges = [[] for _ in range(N)]

    def add_edge(self, s: int, t: int, cap: int) -> None:
        e = [t, cap, None]
        e[2] = erev = [s, 0, e]
        self.edges[s].append(e)
        self.edges[t].append(erev)

    def bfs(self, s: int, t: int) -> bool:
        self.level = [-1] * self.N
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            lnxt = self.level[v] + 1
            for to, cap, _ in self.edges[v]:
                if cap and self.level[to] < 0:
                    self.level[to] = lnxt
                    q.append(to)
        return self.level[t] >= 0

    def dfs_dinic(self, v: int, goal: int, f: int) -> int:
        if v == goal:
            return f
        
        for e in self.it[v]:
            to, cap, rev = e
            if cap and self.level[v] < self.level[to]:
                d = self.dfs_dinic(to, goal, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def Dinic(self, s: int, t: int, req: int) -> int:
        flow = 0
        while self.bfs(s, t) and req:
            *self.it, = map(iter, self.edges)
            while req:
                f = self.dfs_dinic(s, t, req)
                if f == 0:
                    break
                flow += f
                req -= f
        return flow
