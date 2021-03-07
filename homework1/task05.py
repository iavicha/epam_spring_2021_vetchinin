"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List
from collections import deque
import itertools


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k <= 0:
        exit('Think')

    result = []
    nums = deque(nums)

    while len(nums) > 0:
        for one in range(1, k + 1):
            result.append(sum(list(itertools.islice(nums, one))))
        nums.popleft()
    return max(result)
