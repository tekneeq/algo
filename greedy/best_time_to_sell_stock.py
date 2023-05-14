"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    # [7, 1, 5, 3, 6, 4]
    # 5
    # max profit: 6 - 1

    left = 0
    cur_profit, max_profit = 0, 0

    for i, v in enumerate(prices):
        if v < prices[left]:
            left = i
            continue

        cur_profit = v - prices[left]
        if cur_profit > max_profit:
            max_profit = cur_profit

    return max_profit


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
