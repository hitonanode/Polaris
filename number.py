from typing import Tuple


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """Solve ax + by = gcd(a, b)

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    Tuple[int, int, int]
        (d, x, y), d = gcd(a, b)
    """
    d = a
    if b:
        d, y, x = extgcd(b, a % b)
        y -= a // b * x
    else:
        x, y = 1, 0
    return d, x, y


def mod_inverse(a: int, m: int) -> int:
    """Calculate x s.t. ax = gcd(a, m) MOD m

    Parameters
    ----------
    a : int
    m : int

    Returns
    -------
    int
        x s.t. ax = gcd(a, m) MOD m
    """
    _, x_, _ = extgcd(a, m)
    x_ %= m
    return x_ + (x_ < 0) * m
