from array.problem.median_two_arrays import findMedianSortedArrays


def test_find_median_sorted_arrays():
    assert findMedianSortedArrays([1,3], [2]) == 2.0
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5
