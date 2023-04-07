from typing import List


def maxSubArray(nums: List[int]) -> int:
    # [-2,1,-3,4,-1,2,1,-5,4]
    def kadane():
        max_sum = nums[0]
        current_sum = 0

        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = 0


            current_sum += nums[i]

            if current_sum > max_sum:
                max_sum = current_sum


        return max_sum


    def dp():
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)

    return dp()