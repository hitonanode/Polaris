class DSU:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        self.sz = [1] * N
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.par[y] = x
        self.sz[x] += self.sz[y]
        return True
