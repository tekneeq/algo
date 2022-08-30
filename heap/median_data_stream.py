import heapq


class MedianFinder:

    def __init__(self):
        self.nums = []

        self.lo_max_heap = []
        self.hi_min_heap = []

        self.cnt = 0

        self.turn = 1

    # 4
    # lo 4

    # 2
    # lo 2 hi 4

    # 7
    # lo 2 4 hi 7

    # --
    # 7
    # lo 7

    # 2
    # lo 2 hi 7

    # 4
    # lo 2 4 hi 7

    # 1
    # 1, 4, 7      lo [2]   hi []
    # lo [1, 2]   hi [4, 7]

    def addNum(self, num: int) -> None:

        # print(f'adding {num}')

        # 0 means add to lo
        # 1 means add to hi

        self.cnt += 1

        if len(self.lo_max_heap) == 0:
            heapq.heappush(self.lo_max_heap, -num)
            return

        if len(self.hi_min_heap) == 0:
            heapq.heappush(self.hi_min_heap, num)
            return

        lo_num = -(heapq.heappop(self.lo_max_heap))
        hi_num = heapq.heappop(self.hi_min_heap)

        nums_to_add = [num, lo_num, hi_num]
        nums_to_add = sorted(nums_to_add)
        if self.turn == 1:
            # add two nums to lo

            heapq.heappush(self.lo_max_heap, -nums_to_add[0])
            heapq.heappush(self.lo_max_heap, -nums_to_add[1])

            heapq.heappush(self.hi_min_heap, nums_to_add[2])


        else:
            # add two nums to hi

            heapq.heappush(self.lo_max_heap, -nums_to_add[0])

            heapq.heappush(self.hi_min_heap, nums_to_add[1])
            heapq.heappush(self.hi_min_heap, nums_to_add[2])

        self.turn = -self.turn

        return

        # if num < lo_heap[0], add to lo heap
        # move lo_heap[0] to hi_heap

        # else
        # add num to hi_heap and move hi_heap[0] to lo heap

        def find_idx(num, l, r):

            # handle base cases
            if num < self.nums[0]:
                return 0

            if num > self.nums[-1]:
                return len(self.nums)

            mid = (l + r) // 2

            # print(f'{self.nums} : num to insert {num} : l {l} : r {r} : m {mid} ')

            if self.nums[mid] == num:
                return mid
            else:
                if self.nums[mid] < num and self.nums[mid + 1] > num:
                    return mid + 1
                elif self.nums[mid] > num and self.nums[mid - 1] < num:
                    return mid
                else:
                    if num < self.nums[mid]:
                        return find_idx(num, l, mid)
                    else:
                        return find_idx(num, mid, r)

        # start of outer func
        if not self.nums:
            self.nums.append(num)
            return

        idx = find_idx(num, 0, len(self.nums))

        if idx == len(self.nums):
            self.nums.append(num)
        else:

            left = self.nums[:idx]
            right = self.nums[idx:]

            # print(f'\tl {left}, r {right}')
            left.append(num)

            self.nums = left + right

        # print(f'\tNew nums are {self.nums}')

    def findMedian(self) -> float:

        # print(f'{self.cnt} {self.lo_max_heap}')

        if self.cnt % 2 == 0:
            # mid of lo and hi
            lo_num = -(heapq.heappop(self.lo_max_heap))
            hi_num = heapq.heappop(self.hi_min_heap)

            heapq.heappush(self.lo_max_heap, -lo_num)
            heapq.heappush(self.hi_min_heap, hi_num)

            return (lo_num + hi_num) / 2
        else:
            # lo
            lo_num = -(heapq.heappop(self.lo_max_heap))
            heapq.heappush(self.lo_max_heap, -lo_num)

            return lo_num

        # ===

        if len(self.nums) == 2:
            return (self.nums[0] + self.nums[1]) / 2

        mid = len(self.nums) // 2

        if len(self.nums) % 2 == 0:
            median = (self.nums[mid - 1] + self.nums[mid]) / 2
        else:
            median = self.nums[mid]

        # print(f'{self.nums} : {mid} : {median}')

        return median