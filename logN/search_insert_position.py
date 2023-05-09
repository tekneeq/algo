# 35 Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# nums = [1,3,5,6], target = 5 ==> 2
# nums = [1,3,5,6], target = 2 ==> 1
# nums = [1,3,5,6], target = 7 ==> 4
# nums = [1,3,5,6], target = 0 ==> 0


from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    def bin_search(l, r):
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if target > nums[mid] and target <= nums[mid + 1]:
            return mid + 1

        if target < nums[mid]:
            return bin_search(l, mid)
        else:
            return bin_search(mid, r)

    # Base cases
    if target > nums[-1]:
        return len(nums)

    if target < nums[0]:
        return 0

    return bin_search(0, len(nums) - 1)


def searchInsert_editorial(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return left
