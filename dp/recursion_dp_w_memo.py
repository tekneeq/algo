"""
70. Climbing stairs

https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""


def climbStairs(n: int) -> int:
    def step(n, dp):
        if n in dp:
            return dp[n]

        # 1. Exit conditions
        if n == 0:
            return 1

        if n < 0:
            return 0

        # 2. do the permutations
        ways = step(n - 1, dp) + step(n - 2, dp)
        dp[n] = ways
        return ways

    return step(n, {})


def memoize(func):
    mem_dict = {}

    def helper(g):
        if g not in mem_dict:
            mem_dict[g] = func(g)
        return mem_dict[g]

    return helper


@memoize
def climbStairs2(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbStairs2(n - 1) + climbStairs2(n - 2)


assert climbStairs(2) == 2
assert climbStairs(3) == 3


assert climbStairs2(2) == 2
assert climbStairs2(3) == 3
