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


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    if len(nums) <= k: return sum(nums)

    if k <= 0: return 0

    result = []
    nums = deque(nums)
    for i in range(len(nums) + 1):
        if len(nums) >= k:
            result.append(sum(list(nums)[0:3]))
            nums.popleft()
            nums = nums
    return max(result)

