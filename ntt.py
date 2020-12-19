# example: <https://yukicoder.me/submissions/550349>
import numpy as np


class NTT():
    def __init__(self, D: int, MOD: int, root: int) -> None:
        self.md = MOD
        self.w = np.array([1], np.int64)
        self.iw = np.array([1], np.int64)

        while len(self.w) < 1 << (D - 1):
            dw = pow(root, (self.md - 1) // (len(self.w) * 4), self.md)
            dwinv = pow(dw, -1, self.md)
            self.w = np.r_[self.w, self.w * dw] % self.md
            self.iw = np.r_[self.iw, self.iw * dwinv] % self.md

    def ntt(self, mat: np.ndarray):
        in_shape = mat.shape
        n = in_shape[-1]

        m = n // 2
        while m:
            mat = mat.reshape(-1, n // (m * 2), 2, m)
            w_use = self.w[:n // (m * 2)].reshape(1, -1, 1)
            y = mat[:, :, 1] * w_use % self.md
            mat = np.stack((mat[:, :, 0] + y, mat[:, :, 0] + self.md - y), 2) % self.md
            m //= 2
        return mat.reshape(in_shape)

    def intt(self, mat: np.ndarray):
        in_shape = mat.shape
        n = in_shape[-1]

        m = 1
        while m < n:
            mat = mat.reshape(-1, n // (m * 2), 2, m)
            iw_use = self.iw[:n // (m * 2)].reshape(1, -1, 1)
            mat = np.stack((mat[:, :, 0] + mat[:, :, 1], (mat[:, :, 0] + self.md - mat[:, :, 1]) * iw_use), 2) % self.md
            m *= 2
        n_inv = pow(n, -1, self.md)
        return mat.reshape(in_shape) * n_inv % self.md
