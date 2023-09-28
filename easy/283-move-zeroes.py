from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
    """
    i = 0
    p = 0
    while i < len(nums):
        if nums[p] == 0:
            # we do not change 'p' because after poping an element, the current index passes to the next
            nums.append(nums.pop(p))
        else:
            p += 1

        i += 1


if __name__ == '__main__':
    # examples
    moveZeroes(nums=[0, 0, 1])  # [1, 0, 0]
    moveZeroes(nums=[0, 1, 0, 3, 12])  # [1,3,12,0,0]
    moveZeroes(nums=[0])  # [0]
    moveZeroes(nums=[2, 2, 2])  # [2, 2, 2]
