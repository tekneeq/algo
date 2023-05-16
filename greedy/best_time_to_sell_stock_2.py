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
        cur_idx = 0
        valley, peak = prices[0], prices[0]
        maxprofit = 0
        last_idx = len(prices) - 1

        # t([7, 1, 5, 3, 6, 4])
        iter_cnt = 0
        while cur_idx < last_idx:
            iter_cnt += 1
            while cur_idx < last_idx and prices[cur_idx] >= prices[cur_idx + 1]:
                cur_idx += 1

            valley = prices[cur_idx]
            print(f"{iter_cnt} Found valley at idx {cur_idx} with value {valley}")

            while cur_idx < last_idx and prices[cur_idx] <= prices[cur_idx + 1]:
                cur_idx += 1
            peak = prices[cur_idx]

            print(f"{iter_cnt} Found peak at idx {cur_idx} with value {peak}")

            maxprofit += peak - valley
            print(f"{iter_cnt} max profit so far {maxprofit}")

        return maxprofit

    return peak_valley(prices)


ans = maxProfit([7, 1, 5, 3, 6, 4])
assert ans == 7

ans = maxProfit([7, 1, 5, 6, 10, 4])
assert ans == 9


# assert maxProfit([1, 2, 3, 4, 5]) == 4
# assert maxProfit([7, 6, 4, 3, 1]) == 0
