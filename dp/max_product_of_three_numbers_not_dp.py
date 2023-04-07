from typing import List


def maximumProduct(nums: List[int]) -> int:
    from functools import reduce

    def one(nums):
        nums = sorted(nums)

        if len(nums) == 3:
            return reduce((lambda x, y: x * y), nums)

        n_cnt = 0
        p_cnt = 0
        has_zero = False
        for i in nums:
            if i < 0:
                n_cnt += 1
            elif i > 0:
                p_cnt += 1
            else:
                has_zero = True

        # n is 1 or 0, multiply max pos nums
        if n_cnt < 2:
            return reduce((lambda x, y: x * y), nums[-3:])

        if n_cnt >= 2:
            # we know at lest two neg numbs
            neg_product = nums[0] * nums[1]

            if p_cnt == 0:
                if has_zero:
                    return 0
                else:
                    # -4 -3 -2 -1
                    # return the last 3
                    return reduce((lambda x, y: x * y), nums[-3:])

            # p_cnt is 1 and 2
            if p_cnt < 3:
                return neg_product * nums[-1]

            if p_cnt >= 3:
                # fun case, we need to compare
                pos_product = nums[-3] * nums[-2]

                return max(neg_product *nums[-1], pos_product *nums[-1])



    def two(nums):
        A = sorted(nums)
        return max(A[0] *A[1] *A[-1], A[-1] *A[-2] *A[-3])


    return two(nums)