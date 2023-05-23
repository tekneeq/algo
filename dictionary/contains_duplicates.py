"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

"""


from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    def map():
        map = {}

        for i, n in enumerate(nums):
            if not n in map:
                map[n] = []

            map[n].append(i)

        for key, v in map.items():
            shortest = 0
            print(f"k {key}, v {v}")

            if len(v) > 1:
                p = v[0]
                for n in v[1:]:
                    print(f"{n} {p} {n-p} {key}")

                    if n - p <= k:
                        return True

                    p = n

        return False

    def hashmap():
        # when we see a num present in d, we check (if the current index - the index of d[num] ) <= k,
        # we return True, otherwise loop goes on and the duplicate key's value gets updated with current index
        # and ofcourse we return False.
        d = {}
        for i, num in enumerate(nums):
            if (
                num in d and i - d[num] <= k
            ):  # similar to (j - i) <= k, where the i==j(cur idx) and d[num] holds i
                return True
            d[num] = i
        return False

    return hashmap()


assert containsNearbyDuplicate([1, 2, 1], 0) == False
