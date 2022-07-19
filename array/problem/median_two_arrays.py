from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    i, j = 0, 0
    merged_arr = []
    print(f' nums1 len {len(nums1)}, nums2 len {len(nums2)}')
    while i < len(nums1) or j < len(nums2):

        print(f'i {i}, j {j}')

        if i >= len(nums1):
            merged_arr += nums2[j:]
            j = len(nums2)
            continue

        if j >= len(nums2):
            merged_arr += nums1[i:]
            i = len(nums1)
            continue

        if nums1[i] <= nums2[j]:
            merged_arr.append(nums1[i])
            i += 1
        else:
            merged_arr.append(nums2[j])
            j += 1



    median_idx = len(merged_arr) // 2

    print(f'merged arr: {merged_arr}')
    print(f'merged arr len: {len(merged_arr)}')
    print(f'median idx: {median_idx}')

    if len(merged_arr) % 2 == 0:
        return (merged_arr[median_idx] + merged_arr[median_idx-1]) / 2
    else:
        return merged_arr[median_idx]

findMedianSortedArrays([1,3], [2])