class Fenwick:
    """1-indexed Fenwick tree (Binary indexed tree)
    """
    def __init__(self, N: int) -> None:
        self.sz = N + 1
        self.v = [0] * (self.sz)

    def add(self, pos: int, val: int) -> None:
        while pos > 0 and pos < self.sz:
            self.v[pos] += val
            pos += pos & -pos

    def sum(self, pos: int) -> int:
        ret = 0
        while pos:
            ret += self.v[pos]
            pos -= pos & -pos
        return ret
