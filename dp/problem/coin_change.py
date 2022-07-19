"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

ex1
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

ex2
Input: coins = [2], amount = 3
Output: -1

ex3
Input: coins = [1], amount = 0
Output: 0
"""
from typing import List


def coin_change_brute(coins: List[int], amount: int) -> int:
    '''
    1, 2, 5 => 11

    :param coins:
    :param amount:
    :return:
    '''

    def coin_change_internal(idx, coins, amount):
        if amount == 0:
            return 0

        for coin in coins:
            # max num of coins this coin can have
            max_num_coins = coin / amount
            for coin_count in range(max_num_coins):
                coin_sum = coin * coin_count
                leftover_amount = amount - coin_sum

    return coin_change_internal(0, coins, amount)


def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    print(dp)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
            print("coin: %s dp: %s" % (coin, dp))
    return dp[amount] if dp[amount] != float('inf') else -1

print( coin_change([1,2,3], 7))