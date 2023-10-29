from typing import List


def longestSubarray(nums: List[int]) -> int:
    # NOTE: this algorithm is inspired on the solution to challenge
    # "Max Consecutive Ones" from @Timothy H Chang on YouTube
    k = 1
    l = 0

    # iterate over array, r will be the index, n the number or array item
    for r, n in enumerate(nums):
        # deduct 1 from k if n is 0
        k -= 1 - n

        # if we have no supply or k == 0, move the left pointer to the right and add 1 to k (supply) if thr
        if k < 0:
            k += (1 - nums[l])
            l += 1

    return r - l


if __name__ == '__main__':
    longestSubarray(nums=[1, 1, 0, 1])  # 3
    longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1])  # 5
    longestSubarray(nums=[1, 1, 1])  # 0
