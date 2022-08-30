from heap.median_data_stream import MedianFinder


# Your MedianFinder object will be instantiated and called as such:

def test_find_median():
    obj = MedianFinder()

    # 1 3 4 7 8 8 10
    nums = [7, 4, 3, 8, 8, 1, 10]

    for num in nums:
        obj.addNum(num)

    assert obj.findMedian() == 7