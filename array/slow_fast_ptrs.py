from typing import List


foo = [0, 0, 0, 1, 1, 1, 2, 2]


def slow_fast_ptrs(nums: List[int]) -> int:
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            print(f"{[(i,v) for i,v in enumerate(nums)]} {fast}, {slow}")
            # fast 3

            # 0 0 0 1 1 1 2 2
            # 0 1 0 1 1 1 2 2

            nums[slow + 1] = nums[fast]
            slow += 1

        fast += 1

    return nums


def two(nums: List[int]) -> int:
    if not nums:
        return
    slow = fast = 0
    while fast <= len(nums) - 1:
        if nums[fast] != nums[slow]:
            nums[slow + 1] = nums[fast]
            slow += 1
        fast += 1
    return slow + 1


# print("eh")


# print(foo)
# print(slow_fast_ptrs(foo))
print(foo)
print(two(foo))
print(foo)
print("done")


# Remove the elements
# [3, 2, 2, 3]
# => [2, 2, _, _], 2

# [2, 2, 3, 3]
# [3, 3, 2, 2]
# [3, 2, 2, 2]


a = [3, 2, 2, 3]
b = [3, 2, 2, 2]
c = [3, 3, 2, 2]
d = [2, 2, 3, 3]


def two(nums, val):
    i, k = 0, 0

    while k < len(nums):
        if nums[k] != val:
            nums[i] = nums[k]
            i += 1
        k += 1

    return i


print(two(a, 3))
print(two(b, 3))
print(two(c, 3))
print(two(d, 3))
