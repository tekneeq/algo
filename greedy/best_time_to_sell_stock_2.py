"""

122. Best Time to Buy and Sell Stock II (medium)

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

"""


from typing import List


def maxProfit(prices: List[int]) -> int:
    # [7, 1, 5, 3, 6, 4]
    # 1 to 5 = 4
    # 3 to 6 = 3
    # 7

    # [7, 1, 5, 6, 10, 4]
    # 1 to 10 = 9

    # 1) how do we know we sell at 5?
    # 2) how do we know to sell at 10?

    # find lowest bought, then find highest
    # find next lowest lower than the highest

    # 1, 2, 3, 4, 5
    # 1 to 5 = 4
    # 4

    def brute(prices):
        def calc(prices, s):
            if s >= len(prices):
                return 0

            maxx = 0
            for i, v in enumerate(prices):
                maxprofit = 0

                for j, k in enumerate(prices):
                    profit = 0
                    if prices[i] < prices[j]:
                        profit = calc(prices, j + 1) + (prices[j] - prices[i])

                    if profit > maxprofit:
                        maxprofit = profit

                if maxprofit > maxx:
                    maxx = maxprofit

            return maxx

        return calc(prices, 0)

    def peak_valley(prices):
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        last_idx = len(prices) - 1
        while i < last_idx:
            while i < last_idx and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while i < last_idx and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            maxprofit = peak - valley

        return maxprofit

    return peak_valley(prices)


assert maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert maxProfit([1, 2, 3, 4, 5]) == 4
assert maxProfit([7, 6, 4, 3, 1]) == 0
