"""

231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.


-231 <= n <= 231 - 1
"""


def isPowerOfTwo(n: int) -> bool:
    l = 0
    r = 31

    def two(l, r, n):
        mid = (l + r) // 2
        mid_two = 2**mid

        if n == mid_two:
            return True

        if n > mid_two and n < 2 ** (mid + 1):
            return False

        if n < mid_two and n > 2 ** (mid - 1):
            return False

        if n < 2**mid:
            return two(0, mid, n)
        else:
            return two(mid, r, n)

    if n <= 0:
        return False

    return two(0, 31, n)


def isPowerOfTwo_short(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1


def isPowerOfTwo_o_one_o_one(n):
    if n == 0:
        return False
    return n & (-n) == n


def isPowerOfTwo_o_one_o_one_bit_manipulation(n):
    if n == 0:
        return False
    return n & (n - 1) == 0


assert isPowerOfTwo(16) == True
