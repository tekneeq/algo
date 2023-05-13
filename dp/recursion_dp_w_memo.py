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


assert climbStairs(2) == 2
assert climbStairs(3) == 3
