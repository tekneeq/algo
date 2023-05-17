"""
136. Single Number


Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with 
    a linear runtime complexity and 
    use only constant extra space.
"""


from typing import List


def singleNumber(nums: List[int]) -> int:
    # You must implement a solution with a linear runtime complexity and use only constant extra space.

    # what tools do i have to use?

    # 4, 1, 2, 1, 2

    # If we take XOR of zero and some bit, it will return that bit
    # If we take XOR of two same bits, it will return 0

    a = 0
    cnt = 0
    for n in nums:
        cnt += 1
        print(f"{cnt}: a {a}, n {n}")
        a ^= n
        print(f"{cnt}: a {a}")

        print()

    return a


assert singleNumber([4, 1, 2, 1, 2]) == 4
