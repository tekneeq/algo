def myPow(x: float, n: int) -> float:
    # 2**0 == 1
    # 2**1 == 2
    # 2**2 == 4

    # 2**-2
    # 1/x 1/x

    # 2*2*2*2*2    * 2*2*2*2*2
    #  4 * 4* 2      4* 4* 2
    #         2^10
    #      2^5 * 2^5
    # 2^2 * 2^2 *2    * 2^2 * 2^2 * 2
    # 2^1 * 2^1

    def helper(x, n, cmap):
        if n == 1:
            return x

        if n not in cmap:
            half_n = int(n / 2)
            if n % 2 == 0:
                val = helper(x, half_n, cmap) * helper(x, half_n, cmap)
            else:
                val = helper(x, half_n, cmap) * helper(x, half_n, cmap) * x

            cmap[n] = val
            return val
        else:
            return cmap[n]

    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    if n == 1:
        return x

    cmap = {}
    ans = helper(x, int(n / 2), cmap) * helper(x, int(n / 2), cmap)

    if n % 2 == 0:
        return ans

    return ans * x