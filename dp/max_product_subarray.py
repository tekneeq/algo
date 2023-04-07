from typing import List


def maxProduct(nums: List[int]) -> int:
    # [-2,3,-4]
    # [-3,-1,-1]

    if not nums:
        return 0

    dp = [(0, 0) for i in range(len(nums))]
    dp[0] = (nums[0], nums[0])

    for i in range(1, len(nums)):
        # we have calculate min and max of:
        #   keep its number
        #   its number * max of prev num
        #   its number * min of prev num
        max_num = max(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
        min_num = min(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
        dp[i] = (max_num, min_num)

    return max(dp)[0]