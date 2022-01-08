def is_prime(n):
    """
    Miller-Rabin primality test
    Verified: SRM 821 Div.1 1000
    """
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]  # <= 2^64

    def _modpow(x, n, md):
        ret = 1
        x %= md
        while n:
            ret = ret * x % md if (n & 1) else ret
            x = x * x % md
            n = n >> 1
        return ret

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    s = 0
    while ((n - 1) & (1 << s)) == 0:
        s += 1

    for a in bases:
        if a % n == 0:
            continue
        a = _modpow(a, (n - 1) >> s, n)
        may_composite = True
        if a == 1:
            continue
        r = s
        while r:
            r -= 1
            if a == n - 1:
                may_composite = False
            a = a * a % n
        if may_composite:
            return False
    return True
